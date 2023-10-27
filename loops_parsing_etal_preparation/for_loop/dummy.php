<?php
// This is the beginning of a PHP file
// It starts with the opening tag <?php
// You can write comments with // or /* ... */

// Define some variables
$name = "John";
$age = 25;

// Print a greeting message
echo "Hello, $name. You are $age years old.";
?>

		</ol>
		<h3>An unordered list</h3>
		<ul>
			<li>An item in the list</li>
			<li>Another item in the list</li>
			<li>A third item in the list</li>
		</ul>
		<h2>Some links</h2>
		<p>Links are used to connect one web page to another web page or resource. Links are created by using the <a> tag with the href attribute that specifies the URL of the destination. The text between the <a> and </a> tags is the visible part of the link. For example:</p>
		<p>This is a link to <a href="^2^">Bing's homepage</a>.</p>
		<p>This is a link to <a href="^3^">another dummy HTML file</a>.</p>

		<h2>Some images</h2>

		<p>Images are used to add visual interest and information to a web page. Images are inserted by using the <img> tag with the src attribute that specifies the URL of the image source. The alt attribute provides an alternative text for the image in case it cannot be displayed. For example:</p>

		<p>This is an image of Bing's logo: <img src="^4^" alt="Bing logo"></p>

		<p>This is an image of a cat: <img src="^5^" alt="A cat"></p>

		<h2>Some tables</h2>

		<p>Tables are used to display data or information in a structured way. Tables are created by using the <table>, <tr>, <td>, and <th> tags. The <table> tag defines the table element, the <tr> tag defines a table row, the <td> tag defines a table data cell, and the <th> tag defines a table header cell. For example:</p>

		<table border="1">
			<tr><th>Name</th><th>Age</th><th>Pet</th></tr>
			<tr><td>Alice</td><td>25</td><td>Dog</td></tr>
			<tr><td>Bob</td><td>30</td><td>Cat</td></tr>
			<tr><td>Charlie</td><td>35</td><td>Bird</td></tr>
		</table>

		<h2>Some forms</h2>

		<p>Forms are used to collect user input or information. Forms are created by using the <form>, <input>, <label>, <button>, and other tags. The <form> tag defines the form element, the <input> tag defines an input field, the <label> tag defines a label for an input field, and the <button> tag defines a button. For example:</p>

		<form>
			<label for="name">Name:</label>
			<input type="text" id="name" name="name"><br>
			<label for="email">Email:</label>
			<input type="email" id="email" name="email"><br>
			<label for="message">Message:</label>
			<textarea id="message" name="message" rows="4" cols="50"></textarea><br>
			<button type="submit">Send</button>
			<button type="reset">Reset</button>
		</form>

		<h2>Some styles</h2>

<p>Styles are used to change the appearance and layout of a web page. Styles are created by using the <style> tag or the style attribute. The <style> tag defines a style sheet, which is a set of rules that apply to certain elements or classes of elements. The style attribute defines a style for a specific element. Styles use CSS (Cascading Style Sheets) syntax and properties. For example:</p>

<style>
h1 {
	  color: blue;
	    font-family: Arial;
}

p {
	  color: green;
	    font-family: Verdana;
}
<?php
// This is the end of a PHP file
// It ends with the closing tag ?>
// You can omit the closing tag if the file contains only PHP code

// Define a function
function add($x, $y) {
	  return $x + $y;
}

// Call the function and print the result
$result = add(2, 3);
echo "The result is $result.";
?>

