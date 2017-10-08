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
	<td colspan="2" style="text-align: center"><b>Actor (parent)</b></td>
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
		<td> Actor (parent) </td> <td> Actor (parent) </td> <td> Actor (parent) </td> <td> Actor (parent) </td>
	</tr>
	<tr style="text-align: center">
		<td> Item (child) </td> <td> Characters (child) </td> <td> Player (child) </td> <td> Enemies (child)</td>
	</tr>
</table>

<h4> Problems: <h4>

Changes to base (parent) object could break some descendant objects.  <br />
Can quickly turn into a hot mess. 

<h1> Component System </h1>
<h2> Better Option: </h2>

<p> We choose a component system </p>
<p> We 'glue together' different objects -- without a strict hierarchy. There is no parent / child hiearchy <br />
Objects do not inherit code from their parents.  There are no parents </p>

<p>


<h4> How we are going to implement a component system </h4>
<p> Everyhing is an instance of the class Actor().  <p>
<p> When we create our objects (our enemies, items etc.) we then pass other Classes we want to use to Actor().  
<p> This is an example of multiple inheritance in Python. </p>


<table>
	<tr>
		<td> Hero = Actor(Player, Character, Creature)</td>
		<td> Enemy = Actor(Character, Creature, AI)
		<td> Sword = Actor(Item, Weapon)
	</tr>
</table>

<p>

A component sytem gives us more freedom when compared to a strict inheritence system.  <br />
For example an emey may be like our player object but have an AI. Maybe we want a magic spell that makes the player no longer able to control his player avatar
(like a mind control spell).  <br />
To implement our 'mind controll spell' all we need to do is pass (glue on) a "AI" component to the player object.
</p>



