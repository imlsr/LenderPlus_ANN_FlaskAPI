# LenderPlus_ANN_FlaskAPI
Flask API for P2P Lending Neural Network

Public Use : likithlending.herokuapp.com

Returns A Credit Score with a max of 100 and minimum of 0

# Format
1.GET request 
Params include
`loan_amnt` 
`term`
`int_rate`
`annual_inc`

Example : http://127.0.0.1:5000/params?loan_amnt=10000&term=36&int_rate=25.56&annual_inc=100000

2.POST request


RAW Json Format example:


{


    "loan_amnt":10000,
    "term":60,
    "int_rate":5.44,
    "annual_inc":100000


}
