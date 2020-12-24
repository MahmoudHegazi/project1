
from flask import render_template, request, jsonify, flash
from flask_sqlalchemy import SQLAlchemy
from db_class import Band, Event, Comment, db, app
import requests

import os
from flask import Flask, flash, request, redirect, url_for
import sys
from sqlalchemy import desc, asc
from sqlalchemy import text
import string
UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
#ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def query_bands_all():
    bands = Band.query.all()
    return bands

# this function Awesome core script AI
def query_bands_limit(page_number):
    if int(page_number) == 0:
        flash('Error Handle redirect page start number must be > 0 But Do not worry I take care of this')
        page_number = 1
    all_bands = Band.query.all()
    if page_number == 1 or page_number == 0:
        index = 0
    else:
        # if you ask where AI here is
        index =  round((page_number * 9 / page_number) + 1)
        print('asg7t7ya7ya7ast7sa')
        print(index)
    index_end = index + 8
    bands = []
    for item in range(int(len(all_bands))):
        print('item ' + str(item))
        print('index ' + str(index))
        if item >= index:
            print('---------------------------')
            print('item ' + str(item))
            print('index ' + str(index))
            bands.append(all_bands[item])
        if item == index_end:
            return bands
    print(bands)
    return bands

# this function for Pagination events
def query_events_limit(page_number):
    if int(page_number) == 0:
        flash('Error Handle redirect page start number must be > 0 But Do not worry I take care of this')
        page_number = 1
    all_events = Event.query.all()
    if page_number == 1 or page_number == 0:
        index = 0
    else:
        # if you ask where AI here is
        index =  round((page_number * 9 / page_number) + 1)
        print('asg7t7ya7ya7ast7sa')
        print(index)
    index_end = index + 8
    bands = []
    for item in range(int(len(all_events))):
        print('item ' + str(item))
        print('index ' + str(index))
        if item >= index:
            print('---------------------------')
            print('item ' + str(item))
            print('index ' + str(index))
            bands.append(all_events[item])
        if item == index_end:
            return bands
    print(bands)
    return bands


def query_bands_by_limit(limit):
    band = Event.query.order_by(desc(Event.id)).limit(limit).all()
    return band

def query_events_all():
    events = Event.query.all()
    return events

def query_comments_all():
    comments = Comment.query.all()
    return comments

def getBandById(band_id):
    band = Band.query.filter_by(id=band_id).first()
    return band

def getEventById(event_id):
    event = Event.query.filter_by(id=event_id).first()
    return event

def getEventsByBandId(band_id):
    events = Event.query.filter_by(band_id=band_id).all()
    return events


def getBandEvents(band_id):
    result = {'band':None ,'events_list':None,'error':False}
    try:
        result['band'] = Band.query.filter_by(id=band_id).first()
        result['events_list'] = Event.query.filter_by(band_id=band_id).all()
    except:
        result['error'] = True
        print(sys.exc_info())
        db.session.rollback()
    finally:
        result['band'] = None
        result['events_list'] = None

    if result['error'] == True:
        return result
    else:
        return None

def getTopEvent():
    event = Event.query.order_by(asc('id')).first()
    return event

def getUpCommingEvents():
    comming = Event.query.order_by(desc(Event.id)).limit(10).all()
    return comming

def remove_event(event_id):
    error = False
    try:
        event = getEventById(event_id)
        db.session.delete(event)
        db.session.commit()
        db.session.close()
        return True
    except:
        error = True
        print(sys.exc_info())
        db.session.rollback()
    finally:
        db.session.close()
    if not error:
        return True
    else:
        return False


def remove_band(band_id):
    error = False
    try:
        band = getBandById(band_id)
        db.session.delete(band)
        db.session.commit()
        db.session.close()
        return True
    except:
        error = True
        print(sys.exc_info())
        db.session.rollback()
    finally:
        db.session.close()
    if not error:
        return True
    else:
        return False

def getBandIDByEventId(event_id):
    error = False
    try:
        event = Event.query.filter_by(id=event_id).first()
        print(event.id)
        band = Band.query.filter_by(id=event.band_id).first()
    except:
        error = True
        print(sys.exc_info())
        db.session.rollback()
    finally:
        db.session.close()
    if not error:
        return band.id
    else:
        return False

# Game created 1 day ago advanced Game
@app.route('/golden_arrow', methods=['GET'])
def mygame():
    return render_template('golden_arrow.html')

@app.route('/get_like', methods=['GET', 'POST'])
def get_likes():
    event_id = request.get_json()['event_id']
    error = False
    try:
        likes = Event.query.filter_by(id=event_id).first()
        likes_number = likes.like
        print(likes_number)
    except:
        error = True
        print(sys.exc_info())
        db.session.rollback()
    finally:
        db.session.close()
    if not error:
        return jsonify({'like':likes_number,'cod':200})
    else:
        likes_number = 0
        return jsonify({'like':likes_number, 'cod':404})


@app.route('/search_ajax', methods=['POST'])
def search_ajax():
    error = False
    final = []
    subsearch = []
    isband = False
    isevent = False
    search = '%s' % request.get_json()['search']
    print(search.isspace())
    if search.isspace():
        return jsonify({'result':final, 'status':'empty'})
    search = search.lower()
    # i could use better query and use something Like % % but I prefere to do things important on my own

    sql = text('select name, title, id, main_image from Band')
    bands = db.engine.execute(sql)
    sql = text('select id, name, image from Event')
    events = db.engine.execute(sql)
    db.session.close()
    # search if it event
    for object in bands:
        lower_name = object.name.lower()
        lower_title = object.title.lower()
        if lower_name == search:
            print('OMG Found Band')
            url = '/band/' + str(object.id)
            subsearch.append({'name':object.name,'image':object.main_image,'url':url,'type':'Band'})
        elif search in lower_name:
            print('OMG Found Band with elif ')
            url = '/band/' + str(object.id)
            subsearch.append({'name':object.name,'image':object.main_image,'url':url,'type':'Band'})
        else:
            continue
    # search if it event
    for object1 in events:
        lower_name = object1.name.lower()
        if lower_name == search:
            print('OMG Found Event ')
            url = '/event/' + str(object1.id)
            subsearch.append({'name':object1.name,'image':object1.image,'url':url,'type':'Event'})
        elif search in lower_name:
            print('OMG Found Event with elif ')
            url = '/event/' + str(object1.id)
            subsearch.append({'name':object1.name,'image':object1.image,'url':url,'type':'Event'})
        else:
            continue


    if len(final) > 10:
        endresult = final[0:10]
        return jsonify({'result':endresult})
    elif len(final) < 10 and len(subsearch) >= 1:
        for item in subsearch:
            if len(final) == 10:
                return jsonify({'result':final})
            final.append(item)
        return jsonify({'result':final})
    else:
        return jsonify({'result':final, 'status':'empty'})


@app.route('/event/<int:event_id>', methods=['GET','POST'])
def single_event(event_id):

    error = False
    message = ''
    try:
        event = getEventById(event_id)
        this_band_events = getEventsByBandId(event.band_id)
    except:
        error = True
        message = 'Event Not Found'
    finally:
        db.session.close()
    if not error:
        return render_template('event.html', event=event, this_band_events=this_band_events)
    else:
        print('Event Not Found')
        flash('Event Not Found')
        return redirect(url_for('index'))

# edit band
@app.route('/edit_band/<int:band_id>', methods=['GET','POST'])
def edit_band(band_id):
    error = False
    try:
        band = Band.query.filter_by(id=band_id).first()
    except:
        error = True
    finally:
        db.session.close()
    if not error:
        return render_template('edit_band.html', band=band)
    else:
        return redirect(url_for('index', error1="Could not edit the band not Found or deleted"))

# submit form band
@app.route('/submit_edit', methods=['POST'])
def submit_edit_band():
    error = False
    if request.method == 'POST':
        try:
            band_id = request.form.get('band_id')
            itemto_edit = Band.query.filter_by(id=band_id).first()
        except:
            error = True
        finally:
            print('okk')
        if not error:
            name = request.form.get('name')
            title = request.form.get('title')
            band_member_name1 = request.form.get('band_member_name1')
            band_member_name2 = request.form.get('band_member_name2')
            band_member_name3 = request.form.get('band_member_name3')
            email = request.form.get('email')
            mobile = request.form.get('mobile')
            full_desc = request.form.get('full_desc')

            if name:
                try:
                    itemto_edit.name = name
                    db.session.commit()
                except:
                    error = True
                    db.session.rollback()
                finally:
                    print('okk')

            if title:
                try:
                    itemto_edit.title = title
                    db.session.commit()
                except:
                    error = True
                    db.session.rollback()
                finally:
                    print('okk')

            if band_member_name1:
                try:
                    itemto_edit.band_member_name1 = band_member_name1
                    db.session.commit()
                except:
                    error = True
                    db.session.rollback()
                finally:
                    print('okk')

            if band_member_name2:
                try:
                    itemto_edit.band_member_name2 = band_member_name2
                    db.session.commit()
                except:
                    error = True
                    db.session.rollback()
                finally:
                    print('okk')


            if band_member_name3:
                try:
                    itemto_edit.band_member_name3 = band_member_name3
                    db.session.commit()
                except:
                    error = True
                    db.session.rollback()
                finally:
                    print('okk')

            if email and not error:
                try:
                    itemto_edit.email = email
                    db.session.commit()
                except:
                    error = True
                    db.session.rollback()
                finally:
                    print('okk')

            if mobile and not error:
                try:
                    itemto_edit.mobile = mobile
                    db.session.commit()
                except:
                    error = True
                    db.session.rollback()
                finally:
                    print('okk')


            if full_desc and not error:
                try:
                    itemto_edit.full_desc = full_desc
                    db.session.commit()
                except:
                    error = True
                    db.session.rollback()
                finally:
                    print('okk')


            if request.files['main_image'] and request.files['main_image'].filename:
                main_image_object = request.files['main_image']
                filename = main_image_object.filename
                main_image_object.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                main_image= '/' + UPLOAD_FOLDER+'/'+filename
                if main_image and not error:
                    try:
                        itemto_edit.main_image = main_image
                        db.session.commit()
                    except:
                        error = True
                        db.session.rollback()
                    finally:
                        print('okk')


            if request.files['image1'] and request.files['image1'].filename:
                image1_object = request.files['image1']
                filename = image1_object.filename
                image1_object.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                image1= '/' + UPLOAD_FOLDER+'/'+filename
                if image1 and not error:
                    try:
                        itemto_edit.image1 = image1
                        db.session.commit()
                    except:
                        error = True
                        db.session.rollback()
                    finally:
                        print('okk')

            if request.files['image2'] and request.files['image2'].filename:
                image2_object = request.files['image2']
                filename = image2_object.filename
                image2_object.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                image2= '/' + UPLOAD_FOLDER+'/'+filename

                if image2 and not error:
                    try:
                        itemto_edit.image2 = image2
                        db.session.commit()
                    except:
                        error = True
                        db.session.rollback()
                    finally:
                        print('okk')

            if request.files['band_member_image1'] and request.files['band_member_image1'].filename:
                band_member_image1_object = request.files['band_member_image1']
                filename = band_member_image1_object.filename
                band_member_image1_object.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                band_member_image1= '/' + UPLOAD_FOLDER+'/'+filename

                if band_member_image1 and not error:
                    try:
                        itemto_edit.band_member_image1 = band_member_image1
                        db.session.commit()
                    except:
                        error = True
                        db.session.rollback()
                    finally:
                        print('okk')

            if request.files['band_member_image2'] and request.files['band_member_image2'].filename:
                band_member_image2_object =  request.files['band_member_image2']
                filename = band_member_image2_object.filename
                band_member_image2_object.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                band_member_image2= '/' + UPLOAD_FOLDER+'/'+filename

                if band_member_image2 and not error:
                    try:
                        itemto_edit.band_member_image2 = band_member_image2
                        db.session.commit()
                    except:
                        error = True
                        db.session.rollback()
                    finally:
                        print('okk')

            if request.files['band_member_image3'] and request.files['band_member_image3'].filename:
                band_member_image3_object = request.files['band_member_image3']
                filename = band_member_image3_object.filename
                band_member_image3_object.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                band_member_image3= '/' + UPLOAD_FOLDER+'/'+filename

                if band_member_image3 and not error:
                    try:
                        itemto_edit.band_member_image3 = band_member_image3
                        db.session.commit()
                    except:
                        error = True
                        db.session.rollback()
                    finally:
                        print('okk')

            if not error:
                db.session.close()
                flash('Event Edit success')
                return redirect(url_for('index'))
            else:
                db.session.close()
                flash('Event Edit Failure')
                return redirect(url_for('index'))

# edit Event
@app.route('/edit_event/<int:event_id>', methods=['GET','POST'])
def edit_event(event_id):
    bands = query_bands_all()
    error = False
    try:
        event = Event.query.filter_by(id=event_id).first()
    except:
        error = True
        message = 'Event Not Found'
    finally:
        db.session.close()
    if not error:
        return render_template('edit_event.html', event=event, bands=bands)
    else:
        return redirect(url_for('index'))


@app.route('/submit_edit/event', methods=['POST'])
def submit_edit_form():
    error = False
    if request.method == 'POST':
        try:
            event_id = request.form.get('event_id')
            itemto_edit = Event.query.filter_by(id=event_id).first()
        except:
            error = True
        finally:
            print('ok')

        if not error:
            name = request.form.get('name')
            title = request.form.get('title')
            date = request.form.get('date')
            address = request.form.get('address')
            price = request.form.get('price')
            full_desc = request.form.get('full_desc')
            # i will not edit band id
            if name:
                try:
                    itemto_edit.name = name
                    db.session.commit()
                except:
                    error = True
                    print(sys.exc_info())
                    db.session.rollback()
                finally:
                    print('okk')
            if title:
                try:
                    itemto_edit.title = title
                    db.session.commit()
                except:
                    error = True
                    print(sys.exc_info())
                    db.session.rollback()
                finally:
                    print('okk')
            if address:
                try:
                    itemto_edit.address = address
                    db.session.commit()
                except:
                    error = True
                    print(sys.exc_info())
                    db.session.rollback()
                finally:
                    print('okk')

            if price:
                try:
                    itemto_edit.price = price
                    db.session.commit()
                except:
                    error = True
                    print(sys.exc_info())
                    db.session.rollback()
                finally:
                    print('okk')
            if full_desc:
                try:
                    itemto_edit.full_desc = full_desc
                    db.session.commit()
                except:
                    error = True
                    print(sys.exc_info())
                    db.session.rollback()
                finally:
                    print('okk')

            if request.files['image'] and request.files['image'].filename:
                image_object = request.files['image']
                filename = image_object.filename
                image_object.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                image= '/' + UPLOAD_FOLDER+'/'+filename
                print(image)
                if image and not error:
                    try:
                        itemto_edit.image = image
                        db.session.commit()
                    except:
                        error = True
                        print(sys.exc_info())
                        db.session.rollback()
                    finally:
                        print('okk')
            if not error:
                db.session.close()
                flash('Event Edit success')
                return redirect(url_for('index'))
            else:
                db.session.close()
                flash('Event Edit Faluire')
                return redirect(url_for('index'))







    #full_desc, price, address, image, date, title, name,
@app.route('/band/<int:band_id>', methods=['GET','POST'])
def single_band(band_id):
    error = False
    band = getBandById(band_id)
    events = getEventsByBandId(band_id)
    top1 = Band.query.order_by(asc('id')).first()
    bands = query_bands_all()
    return render_template('band.html', band=band, events=events, bands=bands, top1=top1)

@app.route('/remove_band/<int:band_id>', methods=['GET','POST'])
def remove_band(band_id):
    error = False
    events_to_remove =  Event.query.filter_by(band_id=band_id).all()
    for item in events_to_remove:
        try:
            db.session.delete(item)
            db.session.commit()
        except:
            error = True
            print(sys.exc_info())
            db.session.rollback()
        finally:
            db.session.close()
    band_to_remove = Band.query.filter_by(id=band_id).first()
    try:
        db.session.delete(band_to_remove)
        db.session.commit()
    except:
        error = True
        print(sys.exc_info())
        db.session.rollback()
    finally:
        db.session.close()
    if not error:
        flash('Deleted Band success')
        return redirect(url_for('index'))
    else:
        return 'error'




@app.route('/remove_event/<int:event_id>', methods=['GET','POST'])
def remove_the_event(event_id):
    error = False
    bands = query_bands_all()
    events = query_events_all()
    comments = query_comments_all()
    top_event = getTopEvent()
    comming = getUpCommingEvents()
    top1 = Band.query.order_by(asc('id')).first()
    events_to_remove =  Event.query.filter_by(id=event_id).first()
    try:
        db.session.delete(events_to_remove)
        db.session.commit()
    except:
        error = True
        print(sys.exc_info())
        db.session.rollback()
    finally:
        db.session.close()
    flash('remove Event success')
    return redirect(url_for('index'))

#return redirect(url_for('index',bands=bands,events=events,top1=top1,comments=comments,commings=comming))





@app.route('/bandlist', methods=['GET','POST'])
def BandList():
    error = False
    bands = query_bands_all()
    # noob Pagination
    pag = {'max':int(),'list':[], 'pages_number':int(), 'links':[]}
    pag['max'] = int(len(bands))
    pages_number = round(pag['max']/9)
    if pages_number < 1:
        pag['pages_number'] = 1
    else:
        pag['pages_number'] = pages_number
    paglist = []
    for i in range(pag['max']):
        pag['list'].append(i)
    return render_template('band_list.html', bands=bands, pag=pag, current_page=0)

@app.route('/band_list/page/<int:request_start>', methods=['GET','POST'])
def bandList_pag(request_start):
    bands = query_bands_limit(request_start)
    # noob Pagination (It Was Noob 1 day ago But Now IT become Advanced)
    pag_bands = query_bands_all()
    print('jhssssssssssssssssssssss')
    print('jhssssssssssssssssssssss')

    pag = {'max':int(),'list':[], 'pages_number':int(), 'links':[]}
    pag['max'] = int(len(pag_bands))
    pags_links = []
    pages_number = round(pag['max']/9)
    if pages_number < 1:
        pag['pages_number'] = 1
    else:
        pag['pages_number'] = pages_number
    paglist = []
    for i in range(pag['max']):
        pag['list'].append(i)
    if request_start == 0 or request_start == 1:
        current_page = 1
    else:
        current_page = int(request_start)
    print(pag['list'])
    return render_template('band_list.html', bands=bands, pag=pag, current_page=current_page)


@app.route('/event_list/page/<int:request_start>', methods=['GET','POST'])
def event_listpag(request_start):
    events = query_events_limit(request_start)
    # noob Pagination (It Was Noob 1 day ago But Now IT become Advanced)
    pag_bands = query_bands_all()
    print('jhssssssssssssssssssssss')
    print('jhssssssssssssssssssssss')

    pag = {'max':int(),'list':[], 'pages_number':int(), 'links':[]}
    pag['max'] = int(len(pag_bands))
    pags_links = []
    pages_number = round(pag['max']/9)
    if pages_number < 1:
        pag['pages_number'] = 1
    else:
        pag['pages_number'] = pages_number
    paglist = []
    for i in range(pag['max']):
        pag['list'].append(i)
    if request_start == 0 or request_start == 1:
        current_page = 1
    else:
        current_page = int(request_start)
    print(pag['list'])
    return render_template('event_list.html', events=events, pag=pag, current_page=current_page)

@app.route('/home')
@app.route('/')
def index():
    bands = query_bands_all()
    events = query_events_all()
    comments = query_comments_all()
    top_event = getTopEvent()
    comming = getUpCommingEvents()
    top1 = Band.query.order_by(asc('id')).first()
    return render_template('index.html',bands=bands,events=events,top1=top1,comments=comments,commings=comming)



@app.route('/addevent', methods=['GET', 'POST'])
def add_event():
    error = False
    if request.method == 'POST':
        request_name = request.form.get('name')
        s_name = '%s' % request.form.get('name')
        s_title = '%s' % request.form.get('title')
        s_date = '%s' % request.form.get('date')
        s_price = '%s' % request.form.get('price')
        s_address = '%s' % request.form.get('address')
        s_full_desc = '%s' % request.form.get('full_desc')
        s_band_id = '%s' % request.form.get('band_id')
        if request.files['image'] and request.files['image'].filename:
            main_image_object = request.files['image']
            filename = main_image_object.filename
            main_image_object.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            url= '/' + UPLOAD_FOLDER+'/'+filename
            print('Hello Event')
        if s_name and s_title and s_date and s_price and s_address and s_full_desc and s_band_id and url:

            try:
                new_event = Event(name=s_name,title=s_title,date=s_date,price=s_price,address=s_address,full_desc=s_full_desc,band_id=s_band_id,image=url)
                event_name = new_event.name
                db.session.add(new_event)
                db.session.commit()
            except:
                error = True
                print(sys.exc_info())
            finally:
                db.session.close()

            if not error:
                print('New Event added')
                flash('Congts You Created New Event with name %s' % event_name)
                return redirect(url_for('index'))
            else:
                print('Could not add New Event')
                flash('Could not add New Event')
                return redirect(url_for('index'))


@app.route('/add_band', methods=['GET','POST'])
def add_band():

    if request.method == 'POST':
        name = title = main_image = image1  = image2 = band_member_name1 = band_member_image1 = band_member_name2 = band_member_image2 = band_member_name3 = band_member_image3 = email = mobile = full_desc = None
        if request.form.get('name'):
            name = '%s' %     request.form.get('name')

        if request.form.get('title'):
            title = '%s' % request.form.get('title')

        if request.files['main_image'] and request.files['main_image'].filename:
            main_image_object = request.files['main_image']
            filename = main_image_object.filename
            main_image_object.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            main_image= '/' + UPLOAD_FOLDER+'/'+filename

        if request.files['image1'] and request.files['image1'].filename:
            image1_object = request.files['image1']
            filename = image1_object.filename
            image1_object.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            image1= '/' + UPLOAD_FOLDER+'/'+filename

        if request.files['image2'] and request.files['image2'].filename:
            image2_object = request.files['image2']
            filename = image2_object.filename
            image2_object.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            image2= '/' + UPLOAD_FOLDER+'/'+filename

        if request.form.get('band_member_name1'):
            band_member_name1 = '%s' % request.form.get('band_member_name1')


        if request.files['band_member_image1'] and request.files['band_member_image1'].filename:
            band_member_image1_object = request.files['band_member_image1']
            filename = band_member_image1_object.filename
            band_member_image1_object.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            band_member_image1= '/' + UPLOAD_FOLDER+'/'+filename

        if request.form.get('band_member_name2'):
            band_member_name2 = '%s' % request.form.get('band_member_name2')

        if request.files['band_member_image2'] and request.files['band_member_image2'].filename:
            band_member_image2_object =  request.files['band_member_image2']
            filename = band_member_image2_object.filename
            band_member_image2_object.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            band_member_image2= '/' + UPLOAD_FOLDER+'/'+filename

        if request.form.get('band_member_name3'):
            band_member_name3 = '%s' % request.form.get('band_member_name3')


        if request.files['band_member_image3'] and request.files['band_member_image3'].filename:
            band_member_image3_object = request.files['band_member_image3']
            filename = band_member_image3_object.filename
            band_member_image3_object.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            band_member_image3= '/' + UPLOAD_FOLDER+'/'+filename



        if request.form.get('email'):
            email = '%s' % request.form.get('email')


        if request.form.get('mobile'):
            mobile = '%s' % request.form.get('mobile')


        if request.form.get('full_desc'):
            full_desc = '%s' % request.form.get('full_desc')


        if name and title and main_image and image1 and image2 and band_member_name1 and band_member_image1 and band_member_name2 and band_member_image2 and band_member_name3 and band_member_image3 and email and mobile and full_desc:
            new_band = Band(name=name,title=title,main_image=main_image,image1=image1,
            image2=image2,band_member_name1=band_member_name1,
            band_member_image1=band_member_image1,band_member_name2=band_member_name2,
            band_member_image2=band_member_image2,band_member_name3=band_member_name3,
            band_member_image3=band_member_image3, email=email, mobile=mobile,full_desc=full_desc)
            print('good job take break')
            db.session.add(new_band)
            db.session.commit()
            print(new_band)
            print('We Added New band !!')
            flash('Congts You Created New Band with name %s' % new_band.name)
            db.session.close()
            return redirect(url_for('index'))
        else:
            flash('error')
            return redirect(url_for('index'))

    return render_template('add_band.html')


if __name__ == '__main__':
    app.secret_key = 'S&Djry636qyye21777346%%^&&&#^$^^y___'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
