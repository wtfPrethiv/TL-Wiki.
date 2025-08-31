const searchBtn = document.getElementById("search-btn");
const searchPage = document.getElementById("search-page");
const resultsPage = document.getElementById("results-page");

searchBtn.addEventListener("click", () => {

  searchPage.classList.add("hidden");


  setTimeout(() => {
    resultsPage.classList.remove("hidden");
  }, 600);
});
