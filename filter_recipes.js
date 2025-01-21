const categoryFilters = document.querySelectorAll('input[type="checkbox"][name="category"]');
const recipeContainer = document.getElementById('recipe-container');

function filterRecipes(selectedCategories) {
  // Fetch all recipes data from the Django template context (replace with your actual data fetching logic)
  const allRecipes = [ /* your recipe data here */ ]; 

  const filteredRecipes = allRecipes.filter(recipe => {
    return selectedCategories.every(category => recipe.categories.includes(category));
  });

  recipeContainer.innerHTML = ''; 

  filteredRecipes.forEach(recipe => {
    const recipeHTML = `
      <div class="recipe-card">
        <h3>${recipe.title}</h3>
        <p>${recipe.description}</p>
      </div>`;
    recipeContainer.innerHTML += recipeHTML;
  });
}

categoryFilters.forEach(filter => {
  filter.addEventListener('change', () => {
    const selectedCategories = Array.from(categoryFilters)
      .filter(filter => filter.checked)
      .map(filter => filter.dataset.category);
    filterRecipes(selectedCategories);
  });
});