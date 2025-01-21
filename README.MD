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

#### Problems With attempt 1
1. The lambda-CDM model is probably wrong. The local universe, as far as we know, is not homogenous. There are giant voids and superstructures. The universe is clumpy, not homogenous, as far as we know. 
    Therefore, we cannot assume that the average redshift of all points on the celestial sphere is the same.
2. Even if the universe was homogenous, we don't have enough data to make any conclusions using redshift data from objects in the universe. Dividing the celestial sphere into even-sized hexagons, such 
   that each hexagon occupies 1 degree of "latitude" and 1 degree of "longitude", we find that each hexagon contains about ~10 celestial objects. We know from the Hubble Deep Field photograph that that 
   area should contain at least hundreds of thousands of objects that we can photograph. There just hasn't been enough time and resources put to categorizing and organizing data from the celestial sphere. 
