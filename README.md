# Cauldron Meal Planner

A daily, Halloween-flavored meal planner in a single `index.html` (no build step).

- **Household:** one entry per person with their own calorie target (with a built-in calculator). Everyone eats the same meals; portions scale so each person hits their target.
- **Budget & supermarkets (UK):** weekly budget in £, UK supermarkets (Aldi, Lidl, Asda, Tesco, Iceland, Sainsbury's, Morrisons, Ocado, Co-op, Waitrose, M&S) with editable price indexes, supermarket comparison, and day-by-day cost checks. The planner swaps pricey meals for cheaper ones when a day runs over.
- **Preferences:** strict restrictions (vegan, vegetarian, pescatarian, gluten-free, dairy-free, keto), style preferences (healthier, Mediterranean, high protein, budget, quick, comfort, Mexican, Asian, spooky specials), and an avoid list.
- **Daily view:** one "door" per day like a countdown calendar, with swap and lock for each meal.
- **Groceries:** combined shopping list by aisle, in metric with British ingredient names and 400g tins, with checkboxes and copy to clipboard.
- **Recipes:** 45 built-in recipes, plus AI-generated recipes when opened as a Claude artifact.

Open `index.html` in a browser to run it. Data saves to the browser; as a Claude artifact it also syncs to your account.
Prices and price indexes are rough estimates; tune them in Household.

## iPhone home-screen app

`docs/` holds a home-screen (PWA) build served by GitHub Pages: app icon, full-screen launch, and offline support.

- After editing `index.html`, rebuild with `python3 scripts/build-pwa.py` (and `python3 scripts/make-icons.py` to redraw the icon).
- GitHub Pages: Settings → Pages → Deploy from a branch → this branch, folder `/docs`.
- On the iPhone, open the Pages URL in Safari → Share → Add to Home Screen.

The home-screen version saves your plan on the phone only, and AI recipes are available only in the Claude artifact version.
