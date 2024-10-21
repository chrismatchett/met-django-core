# Supercharge Your Django Web Development with Vite.js and Tailwind CSS: Step by Step Guide
**Published:** 1 year ago - **Updated:** 1 year ago  
**5 minutes** - **964 Words**  

## By Shahryar Tayeb  

### Summary  
Learn how to set up Vite with Django 4.x and install Tailwind CSS with this step-by-step guide.

### Related Articles  
- Automatically Generate ERD of Your Django Models  
- How to Split Your Django Project Settings  

## Introduction  
Vite is a build tool that provides a faster and leaner development experience for modern web projects. It comes with two major features:  
- A dev server with rich features and robust HMR (Hot Module Replacement)  
- A build command that bundles your code into optimized assets ready for production  

In this article, we will set up Vite to bundle and serve our Django static files. Let’s begin.

## Project Structure  
You can follow these steps in an old or new Django project without major changes. For this article, we will use a project with the structure below:

```
MYSITE
 > .venv
 > blog
 > mysite
 > static
 > templates
   manage.py
   requirements.txt
```

## Django Static Files Settings  
`mysite/settings.py`  

```python
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
```

## Setup npm  
In the terminal, run the following command to set up npm in the root of the project:

```bash
npm init
```

This will create a `package.json` file with the default content:

```json
{
  "name": "mysite",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC"
}
```

Add the following line to your `package.json`:

```json
{
    ...,
    "type": "module",
}
```

---



Now let's install Vite and Tailwind CSS to our project.

## Install Vite and Tailwind CSS  
Run the following command:

```bash
npm install -D vite tailwindcss postcss autoprefixer django-vite-plugin
```

Initialize Tailwind CSS with the command below. It will create `tailwind.config.js` and `postcss.config.js` files in the root of your application:

```bash
npx tailwindcss init -p
```

Edit the `tailwind.config.js` to specify which files Tailwind should watch for changes:

```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.{html,js}", "./**/templates/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

Make sure you have the templates folder setup in your settings.py

```python
# mysite/settings.py

TEMPLATES = [
    # ...,
    'DIRS': [BASE_DIR / "templates"],
]
```


## Setup Vite  
Create `main.js` and `tailwind.css` files in the static folder at the root of your project:

```javascript
// static/js/main.js
console.log('Js is working');
```

```css
/* static/css/tailwind.css */
@tailwind base;
@tailwind components;
@tailwind utilities;
```

Create a `vite.config.js` file with the created JavaScript and CSS files as input:

```javascript
// vite.config.js
import { defineConfig } from "vite";
import djangoVite from "django-vite-plugin";

export default defineConfig({
  plugins: [
    djangoVite({
      input: ["./static/js/main.js", "./static/css/tailwind.css"],
    }),
  ],
});
```

Add Vite scripts to `package.json`:

```json
"scripts": {
  "test": "echo \"Error: no test specified\" && exit 1",
  "dev": "vite",
  "build": "vite build",
  "preview": "vite preview"
},
```

## Install django-vite-plugin  
We will be using this plugin to configure Vite with our Django backend project. Run:

```bash
pip install django-vite-plugin
```

Add the plugin to `INSTALLED_APPS` in `mysite/settings.py`:

```python
# mysite/settings.py

INSTALLED_APPS = [
	# ...,
	'django_vite_plugin',
]
```

Add the plugin settings and set up templates in Django:

```python
# mysite/settings.py

DJANGO_VITE_PLUGIN = {
    "BUILD_DIR": "staticfiles/build",
    "BUILD_URL_PREFIX": "/" + STATIC_URL + "build",
    "DEV_MODE": True,
}
```

### Explanation of Settings  
- `"BUILD_URL_PREFIX": "/" + STATIC_URL + "build"`: This prefix will be added to our built assets URLs.
- `"DEV_MODE": True`: If true, the routes for the assets will use `http://127.0.0.1:5173`. If false, the plugin will use the compiled version of our assets.

## Load Vite in Templates  
Create a template file:

```html
<!-- templates/blog/main.html -->
<!DOCTYPE html>

{% load vite %}

<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    
    <title>My Django Site</title>

    {% vite 'css/tailwind.css' %}
  </head>

  <body>
    <h2 class="text-red-500 font-bold">This is a template</h2>

    {% vite 'js/main.js' %}
  </body>
</html>
```

I have assumed that you know how to set up URLs and views in Django.

## Run the vite server:

Run the following in a separate terminal:

```bash
    npm run dev
```

## Output  
Tailwind is successfully set up, so let's create a full page.

## Full Tailwind Page  
Let’s get a full Tailwind page from Tailwind components for our home page:  
[Tailwind UI](https://tailwindui.com/components/application-ui/application-shells/stacked)

## Setup for Production Environment  
Build the assets for production. The compiled assets will be in the folder specified in the plugin settings:

```python
DJANGO_VITE_PLUGIN = {
    # ....
    "DEV_MODE": False,
    # ....
}
```

To build the assets, run the following command in your production environment:

```bash
npm run build
```

If you are using a managed hosting provider, you need to change or customize the default build process for your project. For example, Railway uses Nixpacks for building your project and detects the framework automatically.

The problem with our current setup is that we have both `package.json` and `requirements.txt`, so by default, Nix will pick up Node.js and try to build it using Node settings, which will fail.

To customize this, create `nixpacks.toml`:

```toml
providers = ["python","..."]

[phases.build]
cmds = ["echo SHTB_first", "...", "echo SHTB_last"]
```

In the above TOML file, we told Nixpack to first use Python settings, then your auto-detected languages/frameworks. If your `package.json` is inside another folder (such as `static`), use the cmds to build the assets after the Python settings are done.

## Conclusion  
We successfully set up Vite and installed Tailwind CSS on a Django project.
