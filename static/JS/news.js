     var c = 0
     var newsTitle =  {{ newsData|tojson }} ;
     var newsImage =  {{ newsImg|tojson }} ;
     document.getElementById("News-data").innerHTML = newsTitle[c];
     document.getElementById("News-img").src = newsImage[c];

     function disablebtn()
     {
     if (c < 1)
     {
        document.getElementById("Back-Btn").disabled = true;
     }
      else{
        document.getElementById("Back-Btn").disabled = false;
      }
     }
     function nextNews(){
       c = c + 1;
       disablebtn();
       if (newsImage[c] == undefined){
         document.getElementById("Next-Btn").disabled = true;
       }
       else{
         document.getElementById("News-img").src = newsImage[c];
         document.getElementById("News-data").innerHTML = newsTitle[c];
       }

     }
       function prevNews(){
       c = c - 1;
       disablebtn();
       document.getElementById("News-img").src = newsImage[c];
       document.getElementById("News-data").innerHTML = newsTitle[c];

     }
disablebtn();