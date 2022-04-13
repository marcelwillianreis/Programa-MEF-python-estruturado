# Programa-MEF-python-estruturado
 Enter data is from iso q4 element

 This programa is used to calculate simple 2D strutures.
 This programa can use a lot of elements, but enter data was set up to use iso-q4 finit element. 

 To use this programa, it possible to change numbers of: nodes, materials, sections, coodenates, suppot codition and nodal forces.

 The results are presented in stiffness matris, force matrix and displacement matrix. 

 Discplacement matrix can be readed as:
 [x
  y]
 for each node, where x is the displacement nodal in the x axis, and y is the displacement nodal in the y axis. So, for each node there are an couple of x an y coodenates.
 
 For exemple: if there is 2 element with 2 degree of freedon, it can result in 4 degree of freedon for the global strucutre, so displacement matrix result will apear;

 [0.05
  0.01
  0
  0
 ]

 The first tow numebers represents x and y displacements of first node. And the second coupla of numbers (zeros) represents an fixed support.
