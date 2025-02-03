function changeClass(element, classToChange, newClass) {
  element.classList.remove(classToChange);
  element.classList.add(newClass);
}


const btnMenu = document.querySelector('button.hamburger');
const toolbar = document.querySelector('.toolbar');

btnMenu.addEventListener('click', () => {
  if (btnMenu.classList.contains('hamburger--is-active')) {
    changeClass(btnMenu, 'hamburger--is-active', 'hamburger');
    changeClass(toolbar, 'toolbar--is-active', 'toolbar');
  } else {
    changeClass(btnMenu, 'hamburger', 'hamburger--is-active');
    changeClass(toolbar, 'toolbar', 'toolbar--is-active');
  }
})

const menuItems = document.querySelectorAll('.menu a');
menuItems.forEach(item => {
  item.addEventListener("click", () => {
    changeClass(btnMenu, 'hamburger--is-active', 'hamburger');
    changeClass(toolbar, 'toolbar--is-active', 'toolbar');
  })
})
