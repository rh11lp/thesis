from scipy import stats
from scipy.spatial import distance
from scipy import ndimage
import matplotlib.pyplot as plt
import numpy as np



VAEMatrix = np.array([[8.6, 4, 10],		#BeatSaber
					  [8.6, 4, 10],		#SuperHot
					  [8.6, 4, 9],		#SkyrimVR
					  [8.6, 4, 7],		#Moss
					  [4.2, 4, 4],		#Somnai
					  [1.4, 2, 3],		#Pokemon Go
					  [7.1, 10, 10],	#Scary Girl 
					  [8.6, 4.5, 10],	#Surgeon Simulator
					  [8.6, 4.5, 10], 	#Lone Echo
					  [7.1, 4.5, 7], 	#Keep Talking and Nobody Explodes
					  [8.6, 4.5, 9], 	#Employee Recycling Center
					  [8.6, 4, 7], 		#Job Simulator
					  [8.6, 3, 6], 		#Netflix VR
					  [8.6, 4.5, 6], 	#Youtube VR
					  [8.6, 4, 6], 		#Electronauts
					  [8.6, 5.5, 1],	#Samsung Snowboard
                      [8.6, 3.5, 10],   #Gorn
                      [8.6, 3.5, 8],    #Wipeout Omega
                      [8.6, 3.5, 5],    #Tetris Effect
                      [8.6, 3.5, 7],    #Werewolves Within
                      [8.6, 3.5, 6],    #Tumper
					  [8.6, 3.5, 10],	#Eve Valkyrie
					  [8.6, 3.5, 10],	#Sprint Vector
					  [6.5, 6.5, 3],	#Birdly
					  [8.6, 6.5, 8],	#Pro Race VR
					  [8.6, 3.5, 7], 	#Time Travel VR
					  [7.1, 10, 10],	#Amber Sky 2088
					  [7.1, 8.5, 10],	#Arizona Sunshine
					  [7.1, 7.5, 10],	#Ghostbusters Dimension
					  [7.1, 10, 10]		#Dreamscape Immersive
					  ])

#SCIFI MATRIX					  
VAEScifi = np.array([[8.6, 4.5, 9], 	#Employee Recycling Center
					 [7.1, 10, 10],		#Amber Sky 2088
					 [7.1, 7.5, 10],	#Ghostbusters Dimension
					 [7.1, 10, 10]		#Dreamscape Immersive
					])

#SLICE OF LIFE MATRIX
VAESlice = np.array([[8.6, 4, 7]]) #Job Simulator

VAEAction = np.array([[8.6, 4, 10],		#SuperHot
                      [8.6, 3.5, 10],   #Gorn
					  [8.6, 3.5, 10],	#Eve Valkyrie
					  [7.1, 8.5, 10]	#Arizona Sunshine
					])

#RHYTHM MATRIX					
VAERhythm = np.array([[8.6, 4, 6], 		#Electronauts
                      [8.6, 4, 10],		#BeatSaber
                      [8.6, 3.5, 6]    #Tumper
					])					

#LOCATION-BASED
VAELocation = np.array([[1.4, 2, 3],	#Pokemon Go
						[4.2, 4, 4]	#Somnai
					])		


#FANTASY MATRIX					
VAEFantasy = np.array([[8.6, 4, 9],		#SkyrimVR
                      [8.6, 4, 7]		#Moss
					])	

					
#PUZZLE MATRIX					
VAEPuzzle = np.array([[7.1, 4.5, 7], 	#Keep Talking and Nobody Explodes
                      [8.6, 3.5, 5],    #Tetris Effect
					  [8.6, 3.5, 7] 	#Time Travel VR
					])	
					
					
#GENERAL ENTERTAINMENT MATRIX					
VAEGeneral = np.array([[8.6, 3, 6], 		#Netflix VR
					  [8.6, 4.5, 6], 	#Youtube VR
					  [6.5, 6.5, 3]		#Birdly
					])	
					
#SOCIAL/BOARDGAME				
VAESocial = np.array([[8.6, 3.5, 7]])    #Werewolves Within
						
					
#RACING MATRIX					
VAERacing = np.array([[8.6, 3.5, 10],	#Sprint Vector
                      [8.6, 3.5, 8],    #Wipeout Omega
					  [8.6, 6.5, 8]	#Pro Race VR
					])		

	
xVirtuality = VAEMatrix[:,0]
yEncumbrence = VAEMatrix[:,1]
zActivity = VAEMatrix[:,2]

printLinReg = False
printDistance = True
printStanDev = False


#============LINEAR REGRESSION==========================================================================================================================

if printLinReg:

	print('') #newline

	#E > V
	EVslope, EVintercept, EVr_value, EVp_value, EVstd_err = stats.linregress(xVirtuality, yEncumbrence)

	print("Encumbrance as a function of Virtuality")
	print("coefficient of determination: %f" % EVr_value**2)
	print('') #newline

	plt.subplot(311)
	plt.plot(xVirtuality, yEncumbrence, 'o', label='original data')
	plt.plot(xVirtuality, EVintercept + EVslope*xVirtuality, 'r', label='fitted line')
	plt.title("Encumbrance as a function of Virtuality")
	plt.ylabel("Encumbrance")
	plt.xlabel("Virtuality")
	plt.legend()



	#E > A
	EAslope, EAintercept, EAr_value, EAp_value, EAstd_err = stats.linregress(zActivity, yEncumbrence)


	print("Encumbrance as a function of Activity")
	print("coefficient of determination: %f" % EAr_value**2)
	print('') #newline

	plt.subplot(312)
	plt.plot(zActivity, yEncumbrence, 'o', label='original data')
	plt.plot(zActivity, EAintercept + EAslope*zActivity, 'r', label='fitted line')
	plt.title("Encumbrance as a function of Activity")
	plt.ylabel("Encumbrance")
	plt.xlabel("Activity")
	plt.legend()



	#A > V
	AVslope, AVintercept, AVr_value, AVp_value, AVstd_err = stats.linregress(xVirtuality, zActivity)


	print("Activity as a function of Virtuality")
	print("coefficient of determination: %f" % AVr_value**2)
	print('')#newline
	print('No of games: ', VAEMatrix.shape[0])
	print('')#newline
	print('-----------------------------------------------------------------------')

	plt.subplot(313)
	plt.plot(xVirtuality, zActivity, 'o', label='original data')
	plt.plot(xVirtuality, AVintercept + AVslope*xVirtuality, 'r', label='fitted line')
	plt.title("Activity as a function of Virtuality")
	plt.ylabel("Activity")
	plt.xlabel("Virtuality")
	plt.legend()



#============POINT DISTANCE=============================================================================================================================

elif printDistance:

	distanceMatrixAc 	= distance.pdist(VAEAction)
	averageAc			= np.mean(distanceMatrixAc)
	plt.subplot(521)
	plt.hist(distanceMatrixAc, bins='auto')
	plt.title("Action games distance")
	plt.ylabel("Frequency")
	plt.xlabel("Bins")
	
	distanceMatrixGe	= distance.pdist(VAEGeneral)
	averageGe			= np.mean(distanceMatrixGe)
	plt.subplot(522)
	plt.hist(distanceMatrixGe, bins='auto')
	plt.title("GenEnt games distance")
	plt.ylabel("Frequency")
	plt.xlabel("Bins")
	
	distanceMatrixFa	= distance.pdist(VAEFantasy)
	averageFa			= np.mean(distanceMatrixFa)
	plt.subplot(523)
	plt.hist(distanceMatrixFa, bins='auto')
	plt.title("Fantasy games distance")
	plt.ylabel("Frequency")
	plt.xlabel("Bins")
	
	distanceMatrixLo 	= distance.pdist(VAELocation)
	averageLo			= np.mean(distanceMatrixLo)
	plt.subplot(524)
	plt.hist(distanceMatrixLo, bins='auto')
	plt.title("Location-based games distance")
	plt.ylabel("Frequency")
	plt.xlabel("Bins")
	
	distanceMatrixPu 	= distance.pdist(VAEPuzzle)
	averagePu			= np.mean(distanceMatrixPu)	
	plt.subplot(525)
	plt.hist(distanceMatrixPu, bins='auto')
	plt.title("Puzzle games distance")
	plt.ylabel("Frequency")
	plt.xlabel("Bins")
	
	distanceMatrixRa 	= distance.pdist(VAERacing)
	averageRa			= np.mean(distanceMatrixRa)
	plt.subplot(526)
	plt.hist(distanceMatrixRa, bins='auto')
	plt.title("Racing games distance")
	plt.ylabel("Frequency")
	plt.xlabel("Bins")
	
	distanceMatrixRh 	= distance.pdist(VAERhythm)
	averageRh			= np.mean(distanceMatrixRh)
	plt.subplot(527)
	plt.hist(distanceMatrixRh, bins='auto')
	plt.title("Rhythm games distance")
	plt.ylabel("Frequency")
	plt.xlabel("Bins")
	
	distanceMatrixSc 	= distance.pdist(VAEScifi)
	averageSc			= np.mean(distanceMatrixSc)
	plt.subplot(528)
	plt.hist(distanceMatrixSc, bins='auto')
	plt.title("Scifi games distance")
	plt.ylabel("Frequency")
	plt.xlabel("Bins")
	
	#distanceMatrixSl 	= distance.pdist(VAESlice)
	#averageSl			= np.mean(distanceMatrixSl)
	#plt.subplot(529)
	#plt.hist(distanceMatrixSl, bins='auto')
	#plt.title("Slice of life games distance")
	#plt.ylabel("Frequency")
	#plt.xlabel("Bins")
	
	#distanceMatrixSo 	= distance.pdist(VAESocial)
	#averageSo			= np.mean(distanceMatrixSo)
	#plt.subplot(5,2,10)
	#plt.hist(distanceMatrixSo, bins='auto')
	#plt.title("Social games distance")
	#plt.ylabel("Frequency")
	#plt.xlabel("Bins")
	
	
	genreMatrix 		= np.array([averageAc, averageFa, averageGe, averageLo, averagePu, averageRa, averageRh, averageSc]) #, averageSl, averageSo])
	print('Genre matrix: ')
	print(genreMatrix)
	print('')
	
	
	distanceVAE 		= distance.pdist(VAEMatrix)
	distanceVAE			= distance.squareform(distanceVAE)
	averageAll			= np.mean(distanceVAE)
	print('All points distances average: ')
	print(averageAll)
	print('')
	
	print('Standard Deviation between point average distances per genre: ')
	PDstandardDeviation = ndimage.standard_deviation(genreMatrix)
	print(PDstandardDeviation)
	print('')
	
	print('Standard Deviation between overall point distance: ')
	PDstandardDeviation = ndimage.standard_deviation(distanceVAE)
	print(PDstandardDeviation)


	#plt.imshow(averageAll, cmap='hot', interpolation='nearest')

	
#======================STANDARD DEVIATION==================================================================================================================

elif printStanDev:
	print('Standard Deviation: ')
	standardDeviation = ndimage.standard_deviation(VAEMatrix)
	print(standardDeviation)



if printLinReg or printDistance:
	plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=1, hspace=1)
	plt.show()



#python D:\WPy-3670\notebooks\slopetest.py







