# import the libraries
import os
import face_recognition
import cv2

def classify():
    # make a list of all the available images
    files = os.listdir('images')

    dic={}

    ans=1

    #traverse all images in folder
    for i in range(len(files)):
        
        print("In Folder :")
        #if in below extenstion then only used
        if files[i].lower().endswith(('.png', '.jpg', '.jpeg')):
            
            print("In Files :")
            #save orignal image
            orignal=cv2.imread('images/'+files[i])
            # load your image
            blue_image = face_recognition.load_image_file('images/'+files[i])
            
            #face_locations
            face_locations=face_recognition.face_locations(blue_image)
            
            #traverse on faces in image
            for face_location in face_locations:
                
                print('In Face Locations :')
                #face_locations
                top, right, bottom, left = face_location
                
            
                # encoded the loaded image into a feature vector
                
                image_to_be_matched_encoded = face_recognition.face_encodings(blue_image,known_face_locations=[face_location])[0]
                allimage=os.listdir('Allimages')
                # iterate over each image
                
                #flag
                flag=0
                for image in allimage:
                    
                    print("Match Faces in All images :")
                    # load the image
                    im=cv2.imread('Allimages/'+image)
                    
                    
                    
                    # encode the loaded image into a feature vector
                    try:
                        current_image_encoded = face_recognition.face_encodings(im)[0]
                    except:
                        continue
                    # match your image with the image and check if it matches
                    result = face_recognition.compare_faces([image_to_be_matched_encoded], current_image_encoded)
                    # check if it was a match
                    if result[0] == True:
                        
                        print("Image Matched :")
                        cv2.imwrite('People/'+image.split('.')[0]+'/'+files[i],orignal)
                        flag=1
                        break
                if flag==0:
                    
                    print("Images not matched")
                    try:
                        cv2.imwrite('Allimages/'+str(ans)+'.jpg',blue_image[top-30:bottom+30, left-30:right+30])
                    except:
                        cv2.imwrite('Allimages/'+str(ans)+'.jpg',blue_image[top:bottom, left:right])
                    dic[str(ans)]=face_location
                    if os.path.exists('People/'+str(ans))==False:
                        os.mkdir('People/'+str(ans))
                        cv2.imwrite('People/'+str(ans)+'/'+files[i],orignal)
                    else:
                        cv2.imwrite('People/'+str(ans)+'/'+files[i],orignal)
                    ans+=1