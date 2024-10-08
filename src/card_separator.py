# Integrantes:
# Leonardo Di Credico         
# Anthony Hlebania            
# Fernando Hiroaki Suzuki     
# Fernando Santos  

# Instruções de Execução: ./run.sh

import numpy
import cv2

# TODO: Parametrize in a config menu
THRESHOLD1 = 23
THRESOLD2 = 20

AREA_THRESOLD = 500
DILATATION = 2

class CardSeparator():
    def __init__(self) -> None:
        pass

    def separate_card(self, frame: numpy.ndarray, mouse_x: int, mouse_y: int) -> tuple[bool, numpy.ndarray, numpy.ndarray]:
        """Receive an image and a position, then return the sucess, the card around the position and the canny image"""
        error_return = (False, numpy.zeros((0,0)), numpy.zeros((0,0)))

        preprocessed_image = self.preprocess_image(frame)
        if(preprocessed_image.size == 0):
            return error_return
        
        # Storage canny  image as attribute to not be freed after return
        self.canny_image = self.get_binary_canny_image(preprocessed_image)
        all_contours = self.get_image_contours(self.canny_image)
        card_contour = self.get_contour_around_point(all_contours, mouse_x, mouse_y)

        if(card_contour == None):
            return (False, self.canny_image, numpy.zeros((0,0)))
        
        separated_card = self.crop_image(frame, card_contour)
        return True, separated_card, self.canny_image

    def preprocess_image(self, image: numpy.ndarray) -> numpy.ndarray:
        """Apply 7x7 gaussian blur on image, then return it on gray scale"""
        blurred_image = cv2.GaussianBlur(image, (7, 7), 1)
        gray_image = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2GRAY)
        return gray_image
    

    def get_binary_canny_image(self, preprocessed_image: numpy.ndarray) -> numpy.ndarray:
        threshold1 = 23
        threshold2 = 20
        
        # Find edges around of image on pos
        canny_image = cv2.Canny(preprocessed_image, threshold1, threshold2)

        kernel = numpy.ones((DILATATION, DILATATION))
        dilatated_image = cv2.dilate(canny_image, kernel, iterations=1)

        #cv2.imshow("canny", dilatated_image)

        return dilatated_image
    
    def get_image_contours(self, canny_image: numpy.ndarray):
        # Get the coordinates from the edges on canny_image
        all_contours, _ = cv2.findContours(canny_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        filtered_contours: list = []
        for contour in all_contours:
            area = cv2.contourArea(contour)
            if area > AREA_THRESOLD:
                filtered_contours.append(contour)

        return filtered_contours 

    def get_contour_around_point(self, all_contours, x: int, y: int):
        """Return the contour of the card at x,y"""
        for contour in all_contours:
            if cv2.pointPolygonTest(contour, (x, y), False) >= 0:

                # Obtenha as coordenadas e dimensões do retângulo delimitador do objeto
                return cv2.boundingRect(contour)
        return None
    
    def crop_image(self,raw_image: numpy.ndarray, contour):
        """Crops the image around the given contour"""
        x, y, w, h = contour
        cropped_image = raw_image[y:y+h, x:x+w].copy()
        #cv2.imshow("crop", cropped_image)
        return cropped_image
        
