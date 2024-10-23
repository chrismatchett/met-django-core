
## Vite

```bash
# npm 7+, extra double-dash is needed:
npm create vite@latest react-app -- --template react
```

```bash
cd react-app
npm install
npm run dev
```

## Tailwind

```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init
```

## tailwind.config.js
```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

## css

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```