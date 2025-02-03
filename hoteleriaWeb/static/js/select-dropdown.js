document.querySelectorAll(".custom-select").forEach(customSelect => {
  const selectBtn = customSelect.querySelector(".select-button");
  const selectedValue = customSelect.querySelector(".selected-value");
  const optionsList = customSelect.querySelectorAll(".select-dropdown li");

  selectBtn.addEventListener("click", () => {
    customSelect.classList.toggle("active");
    selectBtn.setAttribute(
      "aria-expanded",
      selectBtn.getAttribute("aria-expanded") === "true" ? "false" : "true"
    );
  });

  optionsList.forEach((option) => {
    function handler(e) {
      if (e.type === "click" && e.clientX !== 0 && e.clientY !== 0) {
        selectedValue.textContent = this.children[1].textContent;
        customSelect.classList.remove("active");
      }
      if (e.key === "Enter") {
        selectedValue.textContent = this.textContent;
        customSelect.classList.remove("active");
      }
    }

    option.addEventListener("keyup", handler);
    option.addEventListener("click", handler);
  });

  document.addEventListener("click", (e) => {
    if (!customSelect.contains(e.target) && !selectBtn.contains(e.target)) {
      customSelect.classList.remove("active");
      selectBtn.setAttribute("aria-expanded", "false");
    }
  });
});



