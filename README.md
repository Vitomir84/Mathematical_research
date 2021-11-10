### Small mathematical research to master programming

#### [Activation functions](https://github.com/Vitomir84/Mathematical_research/blob/master/Activation_functions.ipynb)

In artificial neural networks, the activation function of a node defines the output of that node given an input or set of inputs. A standard integrated circuit can be seen as a digital network of activation functions that can be "ON" (1) or "OFF" (0), depending on input. This is similar to the linear perceptron in neural networks. However, only nonlinear activation functions allow such networks to compute nontrivial problems using only a small number of nodes, and such activation functions are called nonlinearities. Activation function.ipynb script will plot the most known activation functions (ReLu, Sigmoid, Tangens, Step, Arctan, Gaussian) and show how they work in Python. For some activation function, two different inputs will be used. 

#### [Monte Carlo simulation of the number pi](https://github.com/Vitomir84/Mathematical_research/blob/master/Approximation_of_pi_number.ipynb)

The simulation works on the principle of generating random points in the square of the page r = 1.
Based on the distance of the point of the center of the coordinate system, it is possible to determine whether the point is inside or outside imaginary quarters of a circle. How is a quarter of the surface of a circle r^2\(π*4), and area of square r^2, number  can be approximated as k/m * 4  where k is the number of points within a quarter of a circle and m is the total number of simulated random points. As the number of randomly generated points increases, it is possible to calculate the number π with greater precision at the expense of time efficiency.

#### [Brownian motion](https://github.com/Vitomir84/Mathematical_research/blob/master/Brownian%20motion%20(random%20walk).ipynb)

This script shows the very important statistical concept of random walk in time series. It differes from white noise becease it has some memory, but also a randomness (memory of previous spot). Particles in luquid and in every matter actually behaves accorting to the random walk that is called Brownian motion. 
We succed to have interesting plots of moving of the particles in reality. 


#### [Area of intersected circles](https://github.com/Vitomir84/Mathematical_research/blob/master/Area_of_intersected_circles.ipynb)

This is a very hard task which aim is to calculate area under intersected circles. We will calculate the area of the connected circles based on the Monte Carlo simulation. The area of all non-integer circles will be calculated through the proportion of random points in relation to the area of a square (rectangle).

#### [Bootstrapping function](https://github.com/Vitomir84/Mathematical_research/blob/master/Bootstrapping.ipynb)

When we want to calculate the reliability of some statistical estimation, when the standard error of some estimation is unknown, we can use the bootstrapping. We can calculate our parameter (e.g. mean or median) on our sample. Then we draw new samples from our sample with replacement and calculate our parameter again (e.g. median on every fake sample). Standard deviation of all our new parameters is estimation of the standard error. We than can calculate the reliability of our estimation.

#### [Chaos formula and ploting convergence](https://github.com/Vitomir84/Mathematical_research/blob/master/Formula%20haosa.ipynb)

This is a simple equation  x_n+1_ = x_n * r * (1-x_n)  where x denotes e.g. the proportion of the current population (whether it has reached its size) and r represents the scaling and growth factor. This equation seems to prove that the future is branching out in several different unpredictable directions.
John von Neumann used this algorithm for random number generation. For different values for parameters r and x, the outcomes becomes chaotic. 

#### [Function for calculating integrals with different levels of precision](https://github.com/Vitomir84/Mathematical_research/blob/master/Integral.ipynb)

Very simple functions for calculating integrals (area under curve). 

#### [Optimizing the brute force algorithm to find the shortest path among randomly created points](https://github.com/Vitomir84/Mathematical_research/blob/master/Najkraca%20duz.ipynb)

This is an example of very simple optimisation technique to begginer. Very useful for understanding the meaning of optimisation

#### [Monty Hall's paradox](https://github.com/Vitomir84/Mathematical_research/blob/master/Montiholov%20paradoks.ipynb)

Great and famous problem of conditional probalities.  Many the most clever people did not succeded to solve it. It is the proof that our brain find Bayes counterintuitive as well as concept of conditional probability. In this small script, I solved the problem through simulation to convince everybody that we should change are prior decisions if the proofs change. 

Monty Hall asks you to choose one of three doors. One of the doors hides a prize (ferari) and the other two doors have no prize (goats). You state out loud which door you pick, but you don’t open it right away.Monty opens one of the other two doors, and there is no prize behind it. At this moment, there are two closed doors, one of which you picked. The prize is behind one of the closed doors, but you don’t know which one.

Monty asks you, “Do you want to switch doors?”

The majority of people assume that both doors are equally like to have the prize. It appears like the door you chose has a 50/50 chance. Because there is no perceived reason to change, most stick with their initial choice. At the end, we calculated the odd ratio that proves that changing our prior choice would almost double the probabilities of winning. 

#### [Birthday problem k people in the same room](https://github.com/Vitomir84/Mathematical_research/blob/master/Simulacija%20da%20li%20je%20n%20broj%20osoba%20rodjen%20istog%20datuma.ipynb)

We need to check what is the probability that out of k people at least 2 people were born on the same date during the year. The solution by simulation should converge towards the theoretical solution as the number of iterations increases.


#### [Prime number generation in parallel](https://github.com/Vitomir84/Mathematical_research/blob/master/Paralelizovanje_generisanja_prostih_brojeva.py)

We did parallelisation of process of generating prime numbers. 



