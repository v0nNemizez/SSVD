

var cont = document.getElementById("vlccontainer");

var path = "\"smb://10.13.37.15/MainShare/" + getVariable("video").split("%20").join(" ") + "\"";

cont.innerHTML="<embed type=\"application/x-vlc-plugin\" id=\"vlc\" pluginspage=\"http://www.videolan.org\" width=\"1280\" height=\"720\" src=" + path + " /><p>" + getVariable("video").split("%20").join(" ") + "</p>";

function getVariable(variable) {
       var get = window.location.search.substring(1);
       var vars = get.split("&");
       for (var i=0; i < vars.length; i++) {
               var pair = vars[i].split("=");
               if(pair[0] == variable){
			   return pair[1];
			   }
       }
       return(false);
}