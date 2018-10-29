	(function () {
		var myfunction = function (ev) {
			var liste_id = dict ({'button': 'demo', 'button1': 'demo1', 'button2': 'demo2', 'button3': 'demo3'});
			var x = document.getElementById (liste_id [ev.target.id]);
			if (x.className.indexOf ('w3-show') == -(1)) {
				x.className += ' w3-show';
				var __iterable0__ = liste_id.py_keys ();
				for (var __index0__ = 0; __index0__ < __iterable0__.length; __index0__++) {
					var l = __iterable0__ [__index0__];
					if (l != ev.target.id) {
						var x = document.getElementById (liste_id [l]);
						if (x.className.indexOf ('w3-show') != -(1)) {
							x.className = x.className.py_replace (' w3-show', '');
						}
					}
				}
			}
			else {
				x.className = x.className.py_replace (' w3-show', '');
			}
		};
		try {
			document.getElementById ('button').addEventListener ('click', myfunction);
			document.getElementById ('button1').addEventListener ('click', myfunction);
			document.getElementById ('button2').addEventListener ('click', myfunction);
			document.getElementById ('button3').addEventListener ('click', myfunction);
		}
		catch (__except0__) {
			// pass;
		}
		try {
			window.w3.slideshow ('.texting', 4000);
		}
		catch (__except0__) {
			// pass;
		}
		var mobali = function () {
			var dots = document.getElementsByClassName ('dot');
			var longeur = len (dots);
			var texting = document.getElementsByClassName ('texting');
			for (var i = 0; i < len (dots); i++) {
				dots [i].className = dots [i].className.py_replace (' active', '');
				if (i == longeur - 1) {
					for (var i = 0; i < len (texting); i++) {
						if (texting [i].style.display == 'block') {
							dots [i].className += ' active';
						}
					}
				}
			}
			window.setTimeout (mobali, 4000);
		};
		try {
			mobali ();
		}
		catch (__except0__) {
			// pass;
		}
		try {
			var elements = document.getElementsByClassName ('column');
			var elements2 = document.getElementsByClassName ('cbp-vm-details');
		}
		catch (__except0__) {
			// pass;
		}
		var baring = function () {
			if (document.getElementById ('baring').style.display == 'block') {
				document.getElementById ('baring').style.display = 'none';
			}
			else {
				document.getElementById ('baring').style.display = 'block';
			}
		};
		document.getElementById ('sandwich').addEventListener ('click', baring);
		__pragma__ ('<all>')
			__all__.baring = baring;
			__all__.elements = elements;
			__all__.elements2 = elements2;
			__all__.mobali = mobali;
			__all__.myfunction = myfunction;
		__pragma__ ('</all>')
	}) ();
