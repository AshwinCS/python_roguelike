<h1> Lesson 5 </h1>

<h2> How to structure the 'objects' in our game </h2>


<h3> Two options: </h3>

<b> First Option </b> is a strict inheritence system:

Parents ----> Children
This is a very 'top down' sytem.

In a <b> "Strict Inheritence system" </b> children inherit code from their parents in a clear, hierachial system.

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

<h4> With an <b>"inhertiance system"</b> all children inherit the code from the parents above them. </h4>

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
A inheritance system can quickly turn into a hot mess. 

<h1> Component System </h1>
<h2> Better Option: </h2>

<p> Instead of a <b> Strict Inheritence system</b> we will use a <i><b> a component system </i></b></p>
<p> We will assign ('glue together') different classes to create objects without a strict hierarchy. There is no parent / child hiearchy <br />
Objects can have multiple parents to inherit code from.  This is a modular system.</p>

<br />
<br />
<br />

<h4> How to implement a component system </h4>
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

A component sytem gives us more freedom when compared to a strict inheritence system.  <br /><br />
For example an emey may be like our player object but have an AI. Maybe we want a magic spell that makes the player no longer able to control his player avatar
(like a mind control spell).  <br />
To implement our 'mind controll spell' all we need to do is pass (glue on) a "AI" component to the player object.
</p>

<h2>Making the Player or Enemy Display On Top</h2>
<p>In the draw_game() function pay attention to in what order you are drawing the characters.  If ENEMY.draw() is called before PLAYER.draw() 
the crab will display on top of the Player.  If PLAYER.draw() is called before ENEMY.draw() the player will display on top of the evil, hated crab. 
</p>
<code>
def draw_game():
   # _____          __  __ ______
  # / ____|   /\   |  \/  |  ____|
 # | |  __   /  \  | \  / | |__
 # | | |_ | / /\ \ | |\/| |  __|
 # | |__| |/ ____ \| |  | | |____


    global SURFACE_MAIN

    # clear the surface
    SURFACE_MAIN.fill(constants.COLOR_DEFAULT_BG)

    # draw the map
    draw_map(GAME_MAP)

    #draw the characters
    PLAYER.draw()    
    ENEMY.draw()        

    # update the display
    pygame.display.flip()
</code>

<h3> Make sure to draw the player on top of all other characters </h3>

<h1>Our First Components</h1>
<p>
Make a new component section below "objects."  <br />
Start the names of each compnent classes with com_
<p>
<h3> First 3 Compnents</h3>
<ol>
	<li>com_Creature</li>
	<li>com_Item</li>
	<li>com_Container</li>
</ol>
<code>
#  ______   ______   .___  ___. .______     ______   .__   __.  _______ .__   __. .___________.    _______.
# /      | /  __  \  |   \/   | |   _  \   /  __  \  |  \ |  | |   ____||  \ |  | |           |   /       |
#|  ,----'|  |  |  | |  \  /  | |  |_)  | |  |  |  | |   \|  | |  |__   |   \|  | `---|  |----`  |   (----`
#|  |     |  |  |  | |  |\/|  | |   ___/  |  |  |  | |  . `  | |   __|  |  . `  |     |  |        \   \    
#|  `----.|  `--'  | |  |  |  | |  |      |  `--'  | |  |\   | |  |____ |  |\   |     |  |    .----)   |   
# \______| \______/  |__|  |__| | _|       \______/  |__| \__| |_______||__| \__|     |__|    |_______/    
                                                                           
def com_Creature:
def com_Items:
def com_Container:  
</code>

