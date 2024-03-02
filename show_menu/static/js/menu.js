var activeUrl = window.location.toString()
var arrayElementA = document.querySelectorAll("ul > li > span > a")

for (elem of arrayElementA) {
    if (elem.href == activeUrl) {
        elem.style.color = "green"
        elem.text = elem.text + " <---"
        while (elem.closest("ul").id > 1) {
            var parent = elem.closest("ul")
            parent.style.display = "block"
            elem = parent.closest("li")
        }
        // break
    }
}

function toggleChildren(element) {
    var children = element.nextElementSibling;
    if (children.style.display === "none") {
        children.style.display = "block";
    } else {
        children.style.display = "none";
    }
}

if (alertMessage) {alert(alertMessage.innerHTML)}
// console.log(alertMessage)
// if ("{{ messages|escapejs }}") {alert("{{ messages|escapejs }}")}
