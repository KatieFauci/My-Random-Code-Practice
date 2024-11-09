import json
import math

def calculate_thickness(pages, paper = "Standard copy paper", output_metric="in"):
    '''
    Description: Calcualte the thickness of a text block
    
    Args: 
      pages (number): The number of pages that will be in the text block

      paper (string): The paper type, defaults to Standard copy paper
          Options: 
           - Thin document paper
           - Standard copy paper
           - Standard multiuse paper
           - Standard letterhead paper
    
      output_metric = The measurement type that the result will be returned in, defaults to inches
          Options:
           - in
           - cm
           - mm  
    '''

    if paper  == "Thin document paper":
        bond_weight = 20
        uncoated_text = 50 
        gsm = 75
        microns = 95
    elif paper  == "Standard copy paper":
        bond_weight = 24
        uncoated_text = 60 
        gsm = 90
        microns = 112
    elif paper  == "Standard multiuse paper":
        bond_weight = 28
        uncoated_text = 70 
        gsm = 105
        microns = 131
    elif paper  == "Standard letterhead paper":
        bond_weight = 32
        uncoated_text = 80 
        gsm = 120
        microns = 150

    results_in_cm = (pages*microns)/10000

    if output_metric == "in":
        measurement = results_in_cm/2.54
    elif output_metric == "cm":
        measurement = results_in_cm
    elif output_metric == "mm":
        measurement = results_in_cm*10

    output = {
        "Unit":output_metric,
        "Measurement": measurement,
        "Paper_Details":{
            "Paper_Type": paper,
            "Bond_Weight": bond_weight,
            "Uncoated_Text": uncoated_text,
            "GSM": gsm,
            "Microns": microns,
        }
    }

    return json.dumps(output, indent=4)


def estimate_pages(word_count, est_words_per_page = 250):
    '''
    Description: calculate an estimate of the number of pages that will be used

    Args:
      word_count (number): the number of words in the book

      est_words_per_page (number): an estimate of the number of words per page, defaults to 250 if no value is provided.
    '''
    result = {
        "pages": math.ceil(word_count/est_words_per_page)
    }
    
    return json.dumps(result, indent=4)


def convert_inch_fraction(dec_inch):
    '''
    Description: Converts a decimal value for inches to a fractional equivelent in 16ths
    
    Args: 
      dec_inch (number): value of the inches in a decimal format
    '''

    whole_in = math.floor(dec_inch)
    fraction_in = dec_inch - whole_in

    sixteenths = round(fraction_in * 16)

    result = {
        "Inches": f'{whole_in} + {sixteenths}/16'
    }
    return json.dumps(result, indent=4)



#results = estimate_pages(word_count=104541, est_words_per_page=285)
#results = calculate_thickness(pages=367, paper="Thin document paper", output_metric="in")
results = convert_inch_fraction(1.3726377952755906)

print(results)



