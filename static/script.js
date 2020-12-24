// Toggle between hiding and showing blog replies/comments
window.addEventListener('DOMContentLoaded', (event) => {
function myFunction(id) {
  var x = document.getElementById(id);
  if (x.className.indexOf("w3-show") == -1) {
    x.className += " w3-show";
  } else {
    x.className = x.className.replace(" w3-show", "");
  }
}

function likeFunction(x) {
  x.style.fontWeight = "bold";
  x.innerHTML = "✓ Liked";
}

// add_event submit

const add_event_btn = document.getElementById("add_event_btn");



add_event_btn.addEventListener('click', ()=> {
   price_input.value = Number(price_input.value.replace('$',''));

})

/*

# AJAX Function for Search

*/

let search_form = document.getElementById("search_ajax");
let search_input = document.getElementById("search_ajax_input");
let result = document.getElementById("search_result");
let thebttun = document.getElementById("the_button");
// Check out Form AJAX
let closing_btn = document.getElementById("close_btn1");


closing_btn.addEventListener('click', end_search)

function end_search() {
  document.getElementById('id01').style.display='none';
  document.getElementById('search_ajax_input').value = '';
  remove_all = document.querySelectorAll('.remover');
  remove_all.forEach( (noob_element)=> {
     noob_element.remove();
  });
  let get_result_cnt = document.getElementById("search_result");
  get_result_cnt.innerHTML = '<br /><br />';

}

  search_input.onkeyup = function(e) {
     let checker = document.getElementById('search_ajax_input');
     let results = document.getElementById("search_result");
     if (checker.value == '' ) {
       remove_all = document.querySelectorAll('.remover');
       remove_all.forEach( (noob_element)=> {
          noob_element.remove();
       });

     }

      setTimeout(function(){
    e.preventDefault();
    fetch('/search_ajax', {
      method: 'POST',
      body: JSON.stringify({
        'search': document.getElementById('search_ajax_input').value
      }),
      headers: {
        'Content-Type': 'application/json'
      }
    }).then(function(response) {
         return response.json();
     }).then(function(jsonres){
        results.innerHTML = '<br /><br />';
         // this called supper handle step to add and without it python returl result
        if (jsonres['status'] != 'empty' && document.getElementById('search_ajax_input').value != '') {
        res = jsonres['result']
        console.log(res);
        let fragment = document.createDocumentFragment();
        for (var result=0; result < res.length; result++) {
        let newspan = document.createElement('span');
        let newtext_type = document.createTextNode(res[result]['type']);
        let newtext_name = document.createTextNode(res[result]['name']);
        let newp = document.createElement('p');
        let newimg = document.createElement('img');
        let newlink = document.createElement('a');
        newlink.className = 'remover';
        newimg.src = res[result]['image'];
        newimg.width = '50'
        newimg.height = '50'
        newlink.href = res[result]['url'];
        newspan.style.float = 'right';
        newspan.appendChild(newtext_type);
        newp.appendChild(newimg);
        newp.appendChild(newtext_name);
        newp.appendChild(newspan);
        newlink.appendChild(newp);
        fragment.appendChild(newlink);

      }
      results.appendChild(fragment);


    }

     });


}, 1);

  }


  const the_body = document.querySelector('body');
  const error_message1 = document.querySelector('#error_messages1');
  const error_container1 = document.querySelector('#error_container');

  var urlParams = new URLSearchParams(window.location.search);
  var myParam = urlParams.get('error1');
  if (myParam) {
    error_container1.style.display = 'block';
    error_message1.textContent = 'Sorry You Are Redirected To Home Page Becuase The Band You Search For Deleted '
}

function likefun(){
  let the_likes1 = document.getElementById('get_like_p');
  alert('gi')
 fetch('/get_likes', {
   method: 'POST',
   body: JSON.stringify({
     'event_id': the_likes1.getAttribute("data-event-id")
   }),
   headers: {
     'Content-Type': 'application/json'
   }
 }).then(function(response) {
      return response.json();
  }).then(function(jsonres){

      alert(jsonres['like']);
      alert(jsonres['status']);
  });

}
});
