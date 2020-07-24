const colors = {
  colorHome: "#0073A9",
  colorAdulting: "#59A3AC",
  colorAcademics: "#FBCC80",
  colorSDP: "#E2BEB0",
  colorVancouver: "#EA8392",
  colorUBC: "#002145"
}

$(document).ready(function(){
  checkFooter();
  $('#c-nav-home').hover(function(e) {
    e.stopPropagation();
    $('.c-home-more').finish();
    $('.c-home-more').slideToggle(300);
    }, (function(e) {
      e.stopPropagation();
      $('.c-home-more').finish();
      $('.c-home-more').fadeOut(300);
    })
  );
});

$(window).resize(function() {
  checkFooter();
});

function checkFooter() {
  if(window.screen.width < 500) {
    if (window.location.href.indexOf("academics") > -1) {
      if(document.getElementById("footer-academics") != null) {
        document.getElementById("footer-academics").style.display = 'block';
      }
     } else if (window.location.href.indexOf("adulting") > -1) {
      if(document.getElementById("footer-adulting") != null) {
        document.getElementById("footer-adulting").style.display = 'block';
      }
     } else if (window.location.href.indexOf("sdp") > -1) {
       if(document.getElementById("footer-sdp") != null) {
        document.getElementById("footer-sdp").style.display = 'block';
       }
     } else if (window.location.href.indexOf("vancouver") > -1) {
       if(document.getElementById("footer-vancouver") != null) {
        document.getElementById("footer-vancouver").style.display = 'block';
       }
     } else if (window.location.href.indexOf("ubc") > -1) {
      if(document.getElementById("footer-ubc") != null) {
        document.getElementById("footer-ubc").style.display = 'block';
      }
     } else {
       if(document.getElementById("footer-academics") != null) {
        document.getElementById("footer-academics").style.display = 'block';
       }
       if(document.getElementById("footer-adulting") != null) {
        document.getElementById("footer-adulting").style.display = 'block';
       }
       if(document.getElementById("footer-ubc") != null) {
        document.getElementById("footer-ubc").style.display = 'block';
       }
       if(document.getElementById("footer-vancouver") != null) {
        document.getElementById("footer-vancouver").style.display = 'block';
       }
       if(document.getElementById("footer-sdp") != null) {
        document.getElementById("footer-sdp").style.display = 'block';
       }
     }
  }
}