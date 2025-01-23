# Overview 
**Does light travel at the same speed in all directions?** We don't know. If the speed were the same in all directions, we would say that the speed of light is "isotropic". The reason we don't 
is because we can't measure the "one-way" speed of light. We can only measure the time it takes for light to travel a round trip from an emitter to a reflector and back to the original emitter.
The reason why we can't measure the speed of light from an emitter to a receiver is because, according to General Relativity, we have no way to synchronize the clocks of two observers. Therefore,
the emitter may emit light to a receiver, but since the two observers don't have synchronized clocks, there's no way to calculate the amount of time that passed between the emission and reception of the light.

#### Solution Attempt 1: Using Redshifts in the Celestial Sphere
There may be a way around this dilemma, and it has to do with redshifts. Imagine that there are thousands of suns surrounding the Earth, and they are all equidistant to the Earth. If they are far enough,
we expect the light from these stars to be redshifted. However, if light travels faster in one direction, then we expect to see LESS redshifting from stars that emit light along that direction, toward the Earth.
For example, if the speed of light is infinite in the pure North-South direction then we would expect to see no redshifting from stars located at the North Pole, and a lot of redshifting (more than expected) 
from stars in the South Pole. 

Assuming that the lambda-CDM model of the universe is correct, and the distribution of objects in space is uniform, then we expect the average redshift in all directions from Earth to be roughly the same. If there
is a discrepancy, then that might lead us to think that the speed of light is not isotropic. To find this discrepancy, I followed these steps:

1. gather the [name, redshift] of all objects in the night sky that are recorded on the Simbad database.
2. filter this data to remove any duplicates.
3. get the average redshifts for each pair of coordinates in the celestial sphere.
4. plot the average redshifts as peaks on a sphere, with higher redshifts represented as higher peaks.

#### Results 
![](https://github.com/arsalan0004/Isotropy_of_light/blob/main/graphics/result_attempt1.gif)

#### Analysis 
1. There's a flat strip along the celestial sphere that represents a "data desert". This band corresponds to the parts of the celestial sphere that are blocked by the Milky Way. 
2. While not visible on the plot, it is clear, by looking at the raw data, that there is not enough data to make a conclusion about the isotropy of light speed. See bullet point 2 of the "Problems with Attempt 1" section 

#### Problems With attempt 1
1. The lambda-CDM model is probably wrong. The local universe, as far as we know, is not homogenous. There are giant voids and superstructures. As far as we know, the universe is clumpy and not homogenous. 
    Therefore, we cannot assume that the average redshift of all points on the celestial sphere is the same.
2. Even if the universe was homogenous, we don't have enough data to make any conclusions using redshift data from objects in the universe. Dividing the celestial sphere into even-sized hexagons, such 
   that each hexagon occupies 1 degree of "latitude" and 1 degree of "longitude", we find that each hexagon contains about ~10 celestial objects. We know from the Hubble Deep Field photograph that that 
   area should contain at least hundreds of thousands of objects that we can photograph. There just hasn't been enough time and resources put to categorizing and organizing data from the celestial sphere. 


### Solution attempt 2: Using the Cosmic Microwave Background (CMB) Radiation 
The cosmic microwave background radiation is a picture of the universe when it was very young. At this point in the universe's life, not enough time had passed for 
gravity to create voids and superstructures. Therefore, the universe was almost homogenous. This solves the first problem encountered in attempt #1. Secondly, the redshift of the CMB has been 
extensively documented, so we don't encounter the problem of lack of data that we saw in attempt #1.

#### Problems with Attempt 2
The differences in temperature of the CMB has been attributed to many different processes in the early universe. Therefore, we must subtract the contribution of these processes before we can consider the 
contribution of the speed of light to the effects of redshifting. Of course, even then, the remaining differences cannot be attributed to the difference in the speed of light without corroberating evidence from a different analysis. 
