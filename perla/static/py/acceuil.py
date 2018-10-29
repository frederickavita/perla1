
def myfunction(ev):
    liste_id = {"button":"demo",
                "button1":"demo1",
                "button2":"demo2",
                "button3": "demo3"}
    x = document.getElementById(liste_id[ev.target.id])
    if x.className.indexOf("w3-show") == - 1:
        x.className += " w3-show"
        for l in liste_id.keys():
            if l != ev.target.id:
                x = document.getElementById(liste_id[l])
                if x.className.indexOf("w3-show") != - 1:
                    x.className = x.className.replace(" w3-show", "")
    else:
        x.className = x.className.replace(" w3-show", "")
try:
    document.getElementById('button').addEventListener("click", myfunction)
    document.getElementById('button1').addEventListener("click", myfunction)
    document.getElementById('button2').addEventListener("click", myfunction)
    document.getElementById('button3').addEventListener("click", myfunction)
except:
    pass

try:
    window.w3.slideshow(".texting", 4000)
except:
    pass


def mobali():
    dots = document.getElementsByClassName("dot")
    longeur = len(dots)
    texting = document.getElementsByClassName("texting")
    for i in range(len(dots)):
        dots[i].className = dots[i].className.replace(" active", "")
        if i == longeur - 1:
            for i in range(len(texting)):
                if texting[i].style.display == "block":
                    dots[i].className += " active"
    window.setTimeout(mobali, 4000)

try:
    mobali()
except:
    pass

try:
    elements = document.getElementsByClassName("column")
    elements2 = document.getElementsByClassName("cbp-vm-details")
except:
    pass


def baring():
    if document.getElementById("baring").style.display == "block":
        document.getElementById("baring").style.display = "none"
    else:
        document.getElementById("baring").style.display = "block"    

document.getElementById("sandwich").addEventListener("click", baring)