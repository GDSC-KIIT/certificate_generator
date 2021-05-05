
# DSC-KIIT Certificate Generator

Sending certificates for events has never been more easy 




  


  

    

  
![Logo](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/th5xamgrr6se0x5ro4g6.png)

    
## Installation 
In order to use this you need to allow less secure apps in the E-mail id through which you want to send E-Mail

Find instructions on how to allow less secure apps [here](https://www.youtube.com/watch?v=Ee7PDsbfOUI) then,

Clone the repository and navigate to the directory

```
    git clone https://github.com/DSC-KIIT/certificate_generator.git
    cd certificate_generator
```

Install npm dependencies and requirements.txt
```
    npm install
    pip3 install -r requirements.txt
```
## Usage
Run the server
```
node server
```
Access the web-app by visiting [localhost:8000](http://localhost:8000)



![prew_img](https://github.com/DSC-KIIT/certificate_generator/blob/main/images/prew_img.png)

  

# Format of the input

### Email
This reffers to the Email-Id throgh which you wish to send E-Mails and have enabled less secure apps, Currently this works only for Gmail ID's
### Password
This refers to the password of the above E-mail adress

### Certificate Image
This is the template of the Certificate
.png and .jpeg file are accepted

### Font
This corresponds to the font which will be used to enscribe name on the Certificate template

.ttf files are accepted, Find variety of fonts [here](https://fonts.google.com/)

### CSV File 
This file containg Name and corresponding email adress fo the participants if u choose to use an excel file here instead of .csv you can find instructions below


Please note that the first row should be ```name```  and  `email`
as shown below 
or you can fill up the data in pre-existing [certificateCSV.csv](https://github.com/DSC-KIIT/certificate_generator/blob/main/cert_files/certificateCSV.csv) file and use it

![csv_img](https://github.com/DSC-KIIT/certificate_generator/blob/main/images/csv_img.png)

### Coordinates (x,y)
This reffers to the cordinates on them image template where name should be enscribed 
You can find These co-ordinates through Microsoft-Paint by hovering over the desired postion and the cordinates will be diaplayed in the extreme bottom left as shown below 
![paint_img](https://github.com/DSC-KIIT/certificate_generator/blob/main/images/paint_img.png)

Here the co-ordinates are 990,680

# Track Progress
You can track the progress of sending certificates through the terminal session which you used to run the command `node server` an example is shown below
![ter_img](https://github.com/DSC-KIIT/certificate_generator/blob/main/images/ter_img.png)

## Using a Excel file
By default it expect a CSV file containing a Name and Email adress of participants, howerver we can also make it read from a Excel file by the following tweaks

In the [main.py](https://github.com/DSC-KIIT/certificate_generator/blob/main/main.py) file 

In line 26 replace

 ```df = pd.read_csv('cert_files/certificateCSV.csv')```
with 

```df = pd.read_excel('cert_files/certificateCSV.csv')```

And you are ready to go

## Contributers

- [@uzair-ali10](https://github.com/uzair-ali10/)
- [@sayamsamal](https://github.com/sayamsamal)

  
## License

[MIT](https://choosealicense.com/licenses/mit/)


[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-javascript.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/open-source.svg)](https://forthebadge.com)
