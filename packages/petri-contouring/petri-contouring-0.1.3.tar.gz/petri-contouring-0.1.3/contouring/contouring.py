import glob
import os
import cv2
import numpy as np
import math


def contour_cutter_circ(b_img_list: list[np.ndarray], thrs: int = 15, rplv: int = 255):
    """
    Process a list of images, converting them to grayscale, thresholding, finding contours,
    and fitting ellipses to the largest contour.

    Args:
    - B_img_list (list): List of images to process.
    - thrs (int): Threshold value for binary thresholding.
    - rplv (int): Value to replace above the threshold.

    Returns:
    - list: List of masks with fitted ellipses drawn.
    """

    masks = []
    for image in b_img_list:
        # Check and convert the image to uint8 if necessary
        if image.dtype != np.uint8:
            image = image.astype(np.uint8)

        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, threshold_mask = cv2.threshold(gray_image, thrs, rplv, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(threshold_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        mask = np.zeros_like(gray_image)
        cv2.drawContours(mask, contours, -1, (255, 255, 255), 2)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        mask = np.zeros_like(gray_image)

        try:
            areas = [cv2.contourArea(cnt) for cnt in contours]
            max_index = np.argmax(areas)
            max_contour = contours[max_index]
            ellipse = cv2.fitEllipse(max_contour)
            cv2.ellipse(mask, ellipse, (255, 255, 255), -1)
        except (ValueError, cv2.error):  # You can specify more exceptions if needed.
            pass

        masks.append(mask)
    return masks


def applying_mask(image, mask):
    return cv2.bitwise_and(image, image, mask=mask)
