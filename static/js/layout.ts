let view:any = (window.location.pathname).split('/');
let home_navBar_link:any = document.getElementById('home-navBar-link')
let information_navBar_link:any = document.getElementById('information-navBar-link')
let contact_navBar_link:any = document.getElementById('contact-navBar-link')

switch (view[1]) {
    case "":
       home_navBar_link.classList.add('active');
       break;
    case "information":
        information_navBar_link.classList.add('active');
        break;
    case "contact":
        contact_navBar_link.classList.add('active');
        break;
}
