<h1> Lesson 5 </h1>

<h2> How to structure the 'objects' in our game </h2>


<h3> Two options: </h3>

<b> First Option </b> is a strict inheritence system:

Parents ----> Children
This is a very 'top down' sytem.

In a <b> "Strict Inheritence system" </b> children inherit code from their parents.

<h3> Example: </h3>

<table>
<tr>
	<td colspan="2"><b>Actor (parent)</b></td>
</tr>
<tr>
	<td>Item (child) </td>
	<td>Characters (child) </td>
</tr>
</table>

<p>
Notice how both "Item" are direct descendants of 'Actor'
</p>

<h4> With an <b>"inhertiance system"</b> all children inherit the code from their parents. </h4>

<h2> Example: </h2>
<table>
	<tr style="text-align: center">
		<td> Actor (parent) </td> <td> Actor (parent) </td> <td> Actor (parent) </td>
	</tr>
	<tr style="text-align: center">
		<td> Item </td> <td> Characters </td> <td> Player </td> <td> Enemies </td>
	</tr>
</table>


