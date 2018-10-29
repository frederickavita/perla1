	(function () {
		try {
			var elements = document.getElementsByClassName ('column');
			var elements2 = document.getElementsByClassName ('cbp-vm-details');
		}
		catch (__except0__) {
			// pass;
		}
		var list_view = function () {
			var elements = document.getElementsByClassName ('column');
			var elements2 = document.getElementsByClassName ('cbp-vm-details');
			window.w3.removeClass ('#view', 'w3-text-mybrown');
			window.w3.addClass ('#grid', 'w3-text-mybrown');
			for (var i = 0; i < len (elements); i++) {
				elements [i].style.float = 'left';
			}
			for (var i = 0; i < len (elements2); i++) {
				elements2 [i].style.position = 'static';
				elements2 [i].style.marginLeft = 'auto';
				elements2 [i].style.marginTop = 'auto';
			}
		};
		var grid_view = function () {
			var elements = document.getElementsByClassName ('column');
			var elements2 = document.getElementsByClassName ('cbp-vm-details');
			window.w3.removeClass ('#grid', 'w3-text-mybrown');
			window.w3.addClass ('#view', 'w3-text-mybrown');
			for (var i = 0; i < len (elements); i++) {
				elements [i].style.float = 'none';
			}
			for (var i = 0; i < len (elements2); i++) {
				elements2 [i].style.position = 'absolute';
				elements2 [i].style.marginLeft = '193px';
				elements2 [i].style.marginTop = '86px';
				elements2 [i].style.textOverflow = 'clip';
				elements2 [i].style.whiteSpace = 'normal';
			}
		};
		try {
			document.getElementById ('grid').addEventListener ('click', list_view);
			document.getElementById ('view').addEventListener ('click', grid_view);
		}
		catch (__except0__) {
			// pass;
		}
		try {
			var element_prod = document.getElementsByClassName ('product_image');
		}
		catch (__except0__) {
			// pass;
		}
		var hover = function (ev) {
			document.getElementById ('overl' + ev.target.id).style.opacity = '1';
		};
		var quick_view = function () {
			var tableau = list ([]);
			var element_prod = document.getElementsByClassName ('product_image');
			var element_prod = len (element_prod);
			var css = document.createElement ('style');
			css.py_metatype = 'text/css';
			for (var i = 1; i < element_prod; i++) {
				if (!__in__ ((('#overl' + str (i)) + ':hover') + ',', tableau)) {
					tableau.append ((('#overl' + str (i)) + ':hover') + ',');
				}
			}
			tableau.append (('#overl' + str (element_prod)) + ':hover');
			var a = ''.join (tableau);
			css.innerHTML = a + '{ opacity: 1;cursor:pointer}';
			document.body.appendChild (css);
		};
		var onload = quick_view ();
		var calcule = function () {
			var element_prod1 = document.getElementsByClassName ('column');
			var element_prod = len (element_prod1);
			var e = document.getElementById ('limited');
			var x = e.options [e.selectedIndex].text;
			if (x == '9') {
				if (element_prod > 9) {
					for (var i = 1; i < element_prod; i++) {
						if (i <= 8) {
							element_prod1 [i].style.display = 'block';
						}
						else {
							element_prod1 [i].style.display = 'none';
						}
					}
				}
			}
			else {
				if (x == '15') {
					if (element_prod >= 15) {
						for (var i = 1; i < element_prod; i++) {
							if (i <= 14) {
								element_prod1 [i].style.display = 'block';
							}
							else {
								element_prod1 [i].style.display = 'none';
							}
						}
					}
				}
				else {
					if (x == '30') {
						if (element_prod <= 30) {
							for (var i = 1; i < element_prod; i++) {
								if (i <= 29) {
									element_prod1 [i].style.display = 'block';
								}
								else {
									element_prod1 [i].style.display = 'none';
								}
							}
						}
					}
				}
			}
		};
		document.getElementById ('limited').addEventListener ('change', calcule);
		var prix = function () {
			var tableau_price = list ([]);
			var element = document.getElementsByClassName ('column');
			var price = document.getElementsByClassName ('item_price');
			var vib = function () {
				var __accu0__ = [];
				for (var i = 0; i < len (price); i++) {
					__accu0__.append (tuple ([price [i].innerHTML, i]));
				}
				return __accu0__;
			} ();
			var yid = function () {
				var __accu0__ = [];
				for (var i = 0; i < len (element); i++) {
					__accu0__.append (i);
				}
				return __accu0__;
			} ();
			vib.py_sort ();
			var __iterable0__ = vib;
			for (var __index0__ = 0; __index0__ < __iterable0__.length; __index0__++) {
				var x = __iterable0__ [__index0__];
				var __left0__ = x;
				var l = __left0__ [0];
				var y = __left0__ [1];
				tableau_price.append (y);
			}
			var html_price = function () {
				var __accu0__ = [];
				var __iterable0__ = tableau_price;
				for (var __index0__ = 0; __index0__ < __iterable0__.length; __index0__++) {
					var i = __iterable0__ [__index0__];
					__accu0__.append (element [i].innerHTML);
				}
				return __accu0__;
			} ();
			var __iterable0__ = yid;
			for (var __index0__ = 0; __index0__ < __iterable0__.length; __index0__++) {
				var i = __iterable0__ [__index0__];
				document.getElementsByClassName ('column') [i].innerHTML = '';
				if (i == len (element) - 1) {
					for (var p = 0; p < len (element); p++) {
						document.getElementsByClassName ('column') [p].innerHTML = html_price [p];
					}
				}
			}
		};
		var nom = function () {
			var tableau_titre = list ([]);
			var element = document.getElementsByClassName ('column');
			var title = document.getElementsByClassName ('title');
			var yid = function () {
				var __accu0__ = [];
				for (var i = 0; i < len (element); i++) {
					__accu0__.append (i);
				}
				return __accu0__;
			} ();
			var tab = function () {
				var __accu0__ = [];
				for (var i = 0; i < len (title); i++) {
					__accu0__.append (tuple ([title [i].innerHTML, i]));
				}
				return __accu0__;
			} ();
			tab.py_sort ();
			var __iterable0__ = tab;
			for (var __index0__ = 0; __index0__ < __iterable0__.length; __index0__++) {
				var x = __iterable0__ [__index0__];
				var __left0__ = x;
				var l = __left0__ [0];
				var y = __left0__ [1];
				tableau_titre.append (y);
			}
			var html_title = function () {
				var __accu0__ = [];
				var __iterable0__ = tableau_titre;
				for (var __index0__ = 0; __index0__ < __iterable0__.length; __index0__++) {
					var i = __iterable0__ [__index0__];
					__accu0__.append (element [i].innerHTML);
				}
				return __accu0__;
			} ();
			var __iterable0__ = yid;
			for (var __index0__ = 0; __index0__ < __iterable0__.length; __index0__++) {
				var i = __iterable0__ [__index0__];
				document.getElementsByClassName ('column') [i].innerHTML = '';
				if (i == len (element) - 1) {
					for (var p = 0; p < len (element); p++) {
						document.getElementsByClassName ('column') [p].innerHTML = html_title [p];
					}
				}
			}
		};
		var elementing = '';
		var yab = '';
		var position = function () {
			var yid = function () {
				var __accu0__ = [];
				for (var i = 0; i < len (elementing); i++) {
					__accu0__.append (i);
				}
				return __accu0__;
			} ();
			var __iterable0__ = yid;
			for (var __index0__ = 0; __index0__ < __iterable0__.length; __index0__++) {
				var i = __iterable0__ [__index0__];
				document.getElementsByClassName ('column') [i].innerHTML = '';
				if (i == len (elementing) - 1) {
					for (var p = 0; p < len (elementing); p++) {
						document.getElementsByClassName ('column') [p].innerHTML = yab [p];
					}
				}
			}
		};
		var caching = function () {
			var e = document.getElementById ('selection');
			var fr = e.options [e.selectedIndex].text;
			if (fr == 'Nom') {
				nom ();
			}
			else {
				if (fr == 'Position') {
					position ();
				}
				else {
					if (fr == 'Prix') {
						prix ();
					}
				}
			}
		};
		var initial = function () {
			elementing = document.getElementsByClassName ('column');
			yab = function () {
				var __accu0__ = [];
				for (var i = 0; i < len (elementing); i++) {
					__accu0__.append (elementing [i].innerHTML);
				}
				return __accu0__;
			} ();
		};
		initial ();
		document.getElementById ('selection').addEventListener ('change', caching);
		__pragma__ ('<all>')
			__all__.caching = caching;
			__all__.calcule = calcule;
			__all__.element_prod = element_prod;
			__all__.elementing = elementing;
			__all__.elements = elements;
			__all__.elements2 = elements2;
			__all__.grid_view = grid_view;
			__all__.hover = hover;
			__all__.initial = initial;
			__all__.list_view = list_view;
			__all__.nom = nom;
			__all__.onload = onload;
			__all__.position = position;
			__all__.prix = prix;
			__all__.quick_view = quick_view;
			__all__.yab = yab;
		__pragma__ ('</all>')
	}) ();
