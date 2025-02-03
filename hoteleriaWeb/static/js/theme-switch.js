function calculateSettingAsThemeString({ localStorageTheme, systemSettingDark }) {
  if (localStorageTheme !== null) {
    return localStorageTheme;
  }

  if (systemSettingDark.matches) {
    return "dark";
  }

  return "light";
}

function updateThemeOnHtmlEl(theme) {
  document.querySelector("html").setAttribute("data-theme", theme);
}

// On page load
const toggleSwitch = document.querySelector(".theme-switch input");
const localStorageTheme = localStorage.getItem("theme");
const systemSettingDark = window.matchMedia("(prefers-color-scheme: dark)");
let currentTheme = calculateSettingAsThemeString({ localStorageTheme, systemSettingDark });
updateThemeOnHtmlEl(currentTheme);

toggleSwitch.addEventListener("change", () => {
  const newTheme = currentTheme === "light" ? "dark" : "light";

  localStorage.setItem("theme", newTheme);
  updateThemeOnHtmlEl(newTheme);

  //##############################
  updateContainerErrorColor(newTheme);  // Agregada la llamada a funcion para el color
  //###############################

  currentTheme = newTheme;
});


//###############################
// Funciones agregadas para el error 404

// Función para cambiar el color de .container_error dependiendo del tema
function updateContainerErrorColor(theme) {
  const containerError = document.querySelector(".container_error");
  if (containerError) {
    if (theme === "dark") {
      containerError.style.color = "#fff";  // Texto negro en modo oscuro
    } else {
      containerError.style.color = "#000";  // Texto blanco en modo claro
    }
  }
}
// Cambiar el color de .container_error al cargar la página
updateContainerErrorColor(currentTheme);

//###############################


