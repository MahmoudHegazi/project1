var guide = document.querySelector('#guide');
var endimage = document.querySelector('#endimage');
var endimage1 = document.querySelector('#endimage1');
var warriror_message = document.querySelector('#wmessage');
var monster_message = document.querySelector('#mmessage');

var chat = document.querySelector('#chat');
var score = document.querySelector('#score_text');
var champ = document.querySelector('#champ');
const steps = document.querySelectorAll('.step');
const gamecontainer = document.querySelector('#game_area');
let score_index = 0;
function myFunction(event) {
  if (score_index > 3) {
    champ.src = 'https://i.stack.imgur.com/1dpmw.gif';
       document.querySelectorAll('.monster').forEach( (mon) => {
    mon.src = 'https://www.animatedimages.org/data/media/574/animated-monster-image-0030.gif';

     warriror_message.textContent = "Warrior: That's what I need sad selecton Power Level: 2";
      monster_message.textContent = "Monster: KIll KILL Woooh..";
    })
  }
  if (score_index > 20) {

       warriror_message.textContent = "Warrior: That's what I need Happy Kid Power Level: 3";
      monster_message.textContent = "Monster: LoL Kid I will Eat You OssssHii..";


    champ.src = 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/ef13c91f-432e-4964-9adb-095af2a9ea36/da1fo9o-d4a0743b-006e-4736-80e2-6c5200cb0a6a.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvZWYxM2M5MWYtNDMyZS00OTY0LTlhZGItMDk1YWYyYTllYTM2XC9kYTFmbzlvLWQ0YTA3NDNiLTAwNmUtNDczNi04MGUyLTZjNTIwMGNiMGE2YS5naWYifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.Rl5t0ZuVNZDPi2YseGhmFeJ4ucZh4CJBZ9VqSDqNDJM';

           document.querySelectorAll('.monster').forEach( (mon) => {
    mon.src = 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/502b19e5-ab15-4b14-817c-29c212286c6e/db8wltp-2ed30c54-a823-4949-b476-4e3522d980be.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvNTAyYjE5ZTUtYWIxNS00YjE0LTgxN2MtMjljMjEyMjg2YzZlXC9kYjh3bHRwLTJlZDMwYzU0LWE4MjMtNDk0OS1iNDc2LTRlMzUyMmQ5ODBiZS5naWYifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.pduVwiCgCRGSCFl3BFFoL984cm3VGvLRnc88xbjpzT0';
    })
  }

  if (score_index > 50) {
    champ.src = 'https://64.media.tumblr.com/1bef7a46c8e5acfe80c6e18872e8852e/8e74a27b5a55bf10-4e/s540x810/fbf4ffabedd01abc6e94be64682d8a6d722c4ff3.gifv';


     document.querySelectorAll('.monster').forEach( (mon) => {
    mon.src = 'https://media3.giphy.com/media/5b5BcyHg2EP1JtZQZs/giphy.gif';
    })

           warriror_message.textContent = "Warrior: That's what I need Cute Dpg Power Level: 4";
      monster_message.textContent = "Monster: come give me a Huge..";
  }

  if (score_index > 80) {
    champ.src = 'https://cutewallpaper.org/21/animated-gif-transparent-background/Mario-run-gif-transparent-background-Album-on-Imgur.gif';

         document.querySelectorAll('.monster').forEach( (mon) => {
    mon.src = 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/5fe34483-7c95-45b8-bd41-3b16d399164c/ddayurp-7dbc0555-e00b-4110-b211-f5eb897f304a.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvNWZlMzQ0ODMtN2M5NS00NWI4LWJkNDEtM2IxNmQzOTkxNjRjXC9kZGF5dXJwLTdkYmMwNTU1LWUwMGItNDExMC1iMjExLWY1ZWI4OTdmMzA0YS5naWYifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.n5EIfHavimKY7vTt8r-3HO0SWGOktu85z-XtAczvKjw';
    })

               warriror_message.textContent = "Warrior: . .... OH Yess!  That's what I need Super Mario Power Level: 5";
      monster_message.textContent = "Monster: I Do not care I can see you,...woooooo!..";
  }

  if (score_index > 180) {
    champ.src = 'https://art.pixilart.com/b483fbd97d362cf.gif';

         document.querySelectorAll('.monster').forEach( (mon) => {
    mon.src = 'https://media2.giphy.com/media/5L2hQFpwHXkOlYJyVX/giphy.gif';

  })
                 warriror_message.textContent = "Warrior: . ....Ohhh  Monster!  I got it Dargon Ball Power  Level: 6";
      monster_message.textContent = "Monster: LOL you are Young Dragon ball I will eat you Im real dragon";
  }

  if (score_index > 280) {
    champ.src = 'https://art.pixilart.com/486032322edeb35.gif';

             document.querySelectorAll('.monster').forEach( (mon) => {
    mon.src = 'https://media2.giphy.com/media/jRr2Y37pHcYlRU8EZg/giphy.gif';
  })
                   warriror_message.textContent = "Warrior: . ....Wait Your Are Dead Monster!   Dargon Ball Power Level: 7";
      monster_message.textContent = "Monster: ...wooOOOOOOOOOzzzz!!.";
  }
  if (score_index > 380) {
    champ.src = 'https://pa1.narvii.com/6198/456fa6338d253558efb390bb76f04c0b5e884ec1_00.gif';

             document.querySelectorAll('.monster').forEach( (mon) => {
    mon.src = 'https://64.media.tumblr.com/f489f2492bd2641f8b8540ef57fb3f2d/tumblr_nq7ymstGxa1tgzy56o1_r2_540.gifv';
  })
  }
  if (score_index > 580) {
    champ.src = 'https://pa1.narvii.com/5781/4c822d527adb1edeb4c0a6091ff90897ab713d22_00.gif';

             document.querySelectorAll('.monster').forEach( (mon) => {
    mon.src = 'https://cdna.artstation.com/p/assets/images/images/020/408/642/original/nirah-______-rath-testbob3.gif?1567652951';
  })

                       warriror_message.textContent = "Warrior: what I can do Now With this large monster Level: 8";
      monster_message.textContent = "Monster:...wOOOshhhhhhw!!..";
  }

  if (score_index > 780) {
    champ.src = 'https://i.imgur.com/YMotbZs.gif?noredirect';

     document.querySelectorAll('.monster').forEach( (mon) => {
    mon.src = 'https://i.pinimg.com/originals/6b/36/ef/6b36efdf9f15b7ff394f8a37c255545c.gif';
  })
                     warriror_message.textContent = "Warrior: what I can do Now With this large monster Level: 9";
      monster_message.textContent = "Monster: You Strong But Still Not stronger than me";
  }

  if (score_index > 1000 ) {
    champ.src = 'https://i.gifer.com/ZDcX.gif';

             document.querySelectorAll('.monster').forEach( (mon) => {
    mon.src = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSFmLqJX-Tzp8jxyIZrUp6A5xfLuRvpdBnlTg&usqp=CAU';
  })
                       warriror_message.textContent = "Warrior: Ultimate Power Nothing Can top it : 10";
      monster_message.textContent = "Monster: OMG Dragon Ball Power I can not Fight you I'm scarry ,...dZwZZw!!..";
  }


  if (score_index === 1200 ) {
      gamecontainer.style.display = "none";
      endimage.style.display = "block";
      endimage1.style.display = "block";
      endimage1.style.height = "100px";
      endimage1.style.width = "100px";
      guide.textContent = "You Have Earned The Golden Arrow"
  }
  drop_coins();
     event.target.appendChild(champ);
  // check if there a coin

   if (event.target.className == 'monster') {
     gamecontainer.style.opacity = '.2';
     chat.textContent = "OH: Monster Killed You  got score: " + score_index;
     endgame();

   }

  if (event.target.className == 'coin') {
  let parent = event.target.parentNode;
  event.target.remove();
  parent.appendChild(champ);
  // add 1 to score
  score_index += 1



    chat.textContent = "Greate: You Found a Coin your Score " + score_index;
  score.textContent = score_index;

  } else {
    drop_monster();
  }

  //event.target.style.background = 'white';

}
function drop_coins() {
  let first = Math.floor((Math.random() * 33) + 0);
  let newimage = document.createElement('img');
  newimage.className = 'coin';
  newimage.src = 'https://www.clipartmax.com/png/middle/237-2370984_gold-coin-icon-png-coin-icon-game.png';
  newimage.style.width = '50px';
  newimage.style.height = '50px';
  steps[first].appendChild(newimage);
  steps[first].style.background = "white";
  steps[first].appendChild(newimage);
  steps[first].style.background = "white";



}
function drop_monster() {
  let first = Math.floor((Math.random() * 33) + 0);
  let newimage = document.createElement('img');
  newimage.className = 'monster';
  newimage.src = 'https://i.gifer.com/Yecy.gif';
  newimage.style.width = '50px';
  newimage.style.height = '50px';
  steps[first].appendChild(newimage);
  steps[first].style.background = "rgb(255 230 230)";




}
steps.forEach( (elm) => {elm.addEventListener('click', myFunction )});

function endgame() {
setTimeout(function(){ gamecontainer.style.display = 'none' }, 3000);
}
