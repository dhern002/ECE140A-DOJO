# DOJO 1:

## CSS Basics:
### Structure:
```css
body {
    padding: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    background-color: blanchedalmond;
}
```
Every CSS rule consists of a few parts. There is a selector, property, and value to be assigned to the property. In this example, the selector is ```body```, and this selects any ```body``` elements in the document (there should only be one though). Inside the ```{}``` are the declarations. First, we have the property value ```padding```, and we are assigning it a value of ```0```. All declarations consist of the property name which we want to effect, and the value we want to assign. CSS is relatively more complicated than HTML, as there are a wide range of selectors as well as property values. If you are interested in learning more, please check out the [MDN CSS Docs.](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)
### How to Use:
CSS can be included in a webpage in a few different ways. Firstly, it can be definied directly in the HTML page by using the style tag as shown below.
```html
<style>
    body {
        background-color: blanchedalmond;
    }
</style>
```
Isn't css so cool? You can add all kinds of colors. We choose blanchedalmond because it is the best sounding color.

The snippet above will change the background color of the body tag (essentially the whole visible webpage) to the specified color. CSS supports raw RGB, hex, and other color formats, as well as some pre-defined names.
***
In addition to the style element, CSS can be contained in its own file, separate from the HTML, and then essentially imported by the HTML page.
```html
<head>
    <link rel="stylesheet" href="static/css/index.css">
</head>
```
```css
body {
    background-color: blanchedalmond;
}
```
The ```<link>``` tag tells the browser that it needs to request the stylesheet resource located at ```css/index.css```, and to load it as a stylesheet. Using an external stylesheet is helpful when you have multiple different web-pages and want to share style between them (not having to write the same code multiple times).
***
The last main way CSS can be used in a web-page is inline through the ```style``` attribute on any element in an HTML page.
```html
<body>
    <h1 style="color: red;">Welcome to the ECE 140A Dojo!</h1>
</body>
```
Notice that when inline styling is used, the selector is omitted, and the rule is directly written there. Inline style is useful when trying small tweaks to perfect your layout.
***
The most important part, how do I center items in a webpage? One of the easiest ways to do so is the following.
```css
body {
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
    align-items: center;
}
```