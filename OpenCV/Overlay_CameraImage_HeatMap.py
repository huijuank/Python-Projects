import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import PySimpleGUI as sg

class overlay():
    def __init__(self):
        pass
    
    ################### Set starting position as red pixel (B,G,R) = (<=50, <=50, >=200)
    def get_start_coordinates(self, camera, start_position):
        bgr_vals = []
        for row in range(len(camera)):
            for col in range(len(camera[0])):
                b = camera[row, col, 0]
                g = camera[row, col, 1]
                r = camera[row, col, 2]
                bgr_vals.append([b,g,r])
                if b <= 50 and (g <= 50 and r >= 200):
                    start_position.extend([col, row])
                    return start_position
        
        return self.get_scan_coordinates(camera, start_position)
    
    def click_event_scan(self, event, x, y, flags, start_position):
        
        # checking for left mouse clicks
        if event == cv.EVENT_LBUTTONDOWN:
            start_position.extend([x,y])
            cv.destroyAllWindows()
    
    def get_scan_coordinates(self, camera,start_position):   
        # displaying the image
        cv.imshow('image', camera)
          
        # setting mouse hadler for the image and calling the click_event() function
        cv.setMouseCallback('image', self.click_event_scan, start_position)
          
        # wait for a key to be pressed to exit
        cv.waitKey(0)
          
        # close the window
        cv.destroyAllWindows()
        
        return start_position
        
    def crop_to_scanned_area(self, camera, start_position, length, height, scale_x, scale_y):
        
        [left, bottom] = start_position
        
        # crop to scanned area
        ################### Change Ratio of n pixel=5cm if camera height change
        top = int(bottom - scale_y * height / 5)
        right = int(left +  scale_x * length / 5)
        
        scan = camera[top:bottom+1,left:right+1]
        return scan
    
    def heatmap_lineDetection(self, t_gray_heatmap, x, y, line_coordinates):
        count = last_row = num_of_lines = 0
        for col in range(len(t_gray_heatmap)):
            coordinate_list = []
            for row in range(len(t_gray_heatmap[0])):
                pixel_value = t_gray_heatmap[col][row]
                if pixel_value < 52:
                    #print(pixel_value)
                    coordinate_list.append((col,row)) ### change row, col to index value not pixel value
                    count += 1
                if pixel_value > 51 and last_row < 52:
                    #print(coordinate_list)
                    if len(coordinate_list) >= 0.1*y:
                        line_coordinates.append([coordinate_list[0], coordinate_list[-1]])
                        num_of_lines += 1
                        count = 0
                        coordinate_list = []      
                        #print('1 Column done')
                last_row = pixel_value
                if num_of_lines == 2:
                    (left, bottom) = line_coordinates[0][1]
                    (right, top) = line_coordinates[1][0]
                    heatmap_coordinates = [top,bottom,left+1,right]
                    #print(heatmap_coordinates)
                    return heatmap_coordinates
        
    def create_overlay_layer(self, heatmap, scan, heatmap_coordinates, alpha):
        [top, bottom, left, right] = heatmap_coordinates
        overlay = heatmap.copy()
        output = heatmap.copy()
        (x, y, c) = overlay[top:bottom,left:right].shape
        resized_scan = cv.resize(scan, (y,x))
        overlay[top:bottom,left:right]=resized_scan
        
        cv.addWeighted(overlay, alpha, heatmap, 1 - alpha, 0, output)
        return output
    
    def show_save_images(self, scan, output, filedir, heatmap_file):
        #cv.imshow("Cropped Scan", scan)
        cv.imshow("Overlay", output)
        cv.waitKey(0)
        overlay_file = heatmap_file.replace('.png', '_overlay.png')
        status = cv.imwrite(filedir + '\\' + overlay_file, output)
        print("Overlayed Heatmap saved successfully?:", status)
    
    def get_overlay(self, filedir, camera_file, heatmap_file, length, height):
        camera = cv.imread(filedir + '\\' + camera_file)
        heatmap = cv.imread(filedir + '\\' + heatmap_file)
        gray_heatmap = cv.cvtColor(heatmap, cv.COLOR_BGR2GRAY)
        t_gray_heatmap = gray_heatmap.T
        
        start_position = []
        line_coordinates = [] 
        (x, y) = gray_heatmap.shape
        alpha = 0.3
        scale_x = 470
        scale_y = 460
    
        start_position = self.get_start_coordinates(camera,start_position)
        scan = self.crop_to_scanned_area(camera, start_position, length, height, scale_x, scale_y)
        heatmap_coordinates = self.heatmap_lineDetection(t_gray_heatmap, x, y, line_coordinates)
        output = self.create_overlay_layer(heatmap, scan, heatmap_coordinates, alpha)
        self.show_save_images(scan, output, filedir, heatmap_file)
