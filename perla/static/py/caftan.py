try:
    elements = document.getElementsByClassName("column")
    elements2 = document.getElementsByClassName("cbp-vm-details")
except:
    pass


    
def list_view():
    elements = document.getElementsByClassName("column")
    elements2 = document.getElementsByClassName("cbp-vm-details")
    window.w3.removeClass('#view','w3-text-mybrown')
    window.w3.addClass('#grid','w3-text-mybrown')
    for i in range(len(elements)):
        elements[i].style.float = "left"

    for i in range(len(elements2)):
        elements2[i].style.position = "static"
        elements2[i].style.marginLeft = "auto"
        elements2[i].style.marginTop = "auto"




def grid_view():
    elements = document.getElementsByClassName("column")
    elements2 = document.getElementsByClassName("cbp-vm-details")
    window.w3.removeClass('#grid','w3-text-mybrown')
    window.w3.addClass('#view','w3-text-mybrown')
    for i in range(len(elements)):
        elements[i].style.float = "none"

    for i in range(len(elements2)):
        elements2[i].style.position = "absolute"
        elements2[i].style.marginLeft = "193px"
        elements2[i].style.marginTop = "86px"
        elements2[i].style.textOverflow = "clip"
        elements2[i].style.whiteSpace = "normal"



try:
    document.getElementById("grid").addEventListener("click", list_view)
    document.getElementById("view").addEventListener("click", grid_view)
except:
    pass


try:
    element_prod = document.getElementsByClassName("product_image")
except:
    pass


def hover(ev):
    document.getElementById("overl" + ev.target.id).style.opacity = "1"



def quick_view():
    tableau = []
    element_prod = document.getElementsByClassName("product_image")
    element_prod = len(element_prod)
    css = document.createElement("style")
    css.type = "text/css"
    for i in range(1,element_prod):
        if "#overl" + str(i) + ":hover" +',' not in tableau:
            tableau.append("#overl" + str(i) + ":hover"  +',' )
    tableau.append("#overl" + str(element_prod ) + ":hover")
    a =  ''.join(tableau)
    css.innerHTML = a +  "{ opacity: 1;cursor:pointer}"
    document.body.appendChild(css)


onload = quick_view()

def calcule():
    element_prod1 = document.getElementsByClassName("column")
    element_prod = len(element_prod1)
    e = document.getElementById("limited")
    x = e.options[e.selectedIndex].text
    if x  == "9":
        if element_prod > 9:
           for i in range(1,element_prod):
                   if i <= 8:
                       element_prod1[i].style.display = "block"
                   else:
                       element_prod1[i].style.display = "none"                          
    elif x == "15": 
        if element_prod >= 15:
            for i in range(1,element_prod):
                if i <= 14:
                    element_prod1[i].style.display = "block"
                else:
                    element_prod1[i].style.display = "none" 
    elif x == "30":
        if element_prod <= 30:
            for i in range(1,element_prod):
                if i <= 29:
                    element_prod1[i].style.display = "block"
                else:
                    element_prod1[i].style.display = "none"                  
                




document.getElementById('limited').addEventListener("change",calcule)



 


def prix():
    tableau_price = []
    element = document.getElementsByClassName("column")
    price = document.getElementsByClassName("item_price")
    vib =  [(price[i].innerHTML, i) for i in range(len(price))]
    yid = [i for i in range(len(element))]
    vib.sort()  
    for x in vib:
        (l,y) = x 
        tableau_price.append(y)  
    html_price = [element[i].innerHTML for i in tableau_price]
    for i in yid:
        document.getElementsByClassName("column")[i].innerHTML =""
        if i == len(element)- 1:
            for p in range(len(element)):
                document.getElementsByClassName("column")[p].innerHTML = html_price[p]





def nom():
    tableau_titre = []
    element = document.getElementsByClassName("column")
    title = document.getElementsByClassName("title")
    yid = [i for i in range(len(element))]
    tab =  [(title[i].innerHTML, i) for i in range(len(title))]
    tab.sort()
    for x in tab:
        (l, y) = x
        tableau_titre.append(y)
    html_title = [element[i].innerHTML for i in tableau_titre]      
    for i in yid:
        document.getElementsByClassName("column")[i].innerHTML =""
        if i == len(element)- 1:
            for p in range(len(element)):
                document.getElementsByClassName("column")[p].innerHTML = html_title[p]


elementing = ''
yab = ''
def position():
    global elementing 
    global yab
    yid = [i for i in range(len(elementing))]
    for i in yid:
        document.getElementsByClassName("column")[i].innerHTML =""
        if i == len(elementing)- 1:
            for p in range(len(elementing)):
                document.getElementsByClassName("column")[p].innerHTML = yab[p]

def caching():
    e = document.getElementById("selection")
    fr = e.options[e.selectedIndex].text
    if fr == "Nom":
        nom()
    elif fr == "Position":
        position()   
    elif fr == "Prix":
        prix()     


def initial():
    global elementing
    global yab
    elementing = document.getElementsByClassName("column")
    yab =  [elementing[i].innerHTML for i in range(len(elementing))]

initial()

document.getElementById('selection').addEventListener("change", caching)    

   