(function(e){e.fn.unveil=function(t,n){function f(){var t=u.filter(function(){var t=e(this);if(t.is(":hidden"))return;var n=r.scrollTop(),s=n+r.height(),o=t.offset().top,u=o+t.height();return u>=n-i&&o<=s+i});a=t.trigger("unveil"),u=u.not(a)}var r=e(window),i=t||0,s=window.devicePixelRatio>1,o=s?"data-src-retina":"data-src",u=this,a;return this.one("unveil",function(){var e=this.getAttribute(o);e=e||this.getAttribute("data-src"),e&&(this.setAttribute("src",e),typeof n=="function"&&n.call(this))}),r.scroll(f),r.resize(f),f(),this}})(window.jQuery||window.Zepto);