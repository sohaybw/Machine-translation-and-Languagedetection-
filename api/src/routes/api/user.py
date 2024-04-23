from typing import Any, List
# import email
from fastapi import APIRouter, Body,UploadFile,File ,HTTPException , Form , WebSocket, WebSocketDisconnect
# from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
# from fastapi.responses import StreamingResponse
from DS import run_model ,predict_model
from pydantic import BaseModel
import os 
import json 


router = APIRouter(
    prefix="/user", 
    tags=["User"]
    )

class TextInput(BaseModel):
    text: str

################################# Language Translator #####################################

    
@router.post("/translator")

async def translator(input_data: TextInput): 

    try:
        received_text = input_data.text
        print (type(received_text))

            
       
        translated_result = run_model(received_text)
        



  # Create a dictionary with the input and output texts
        response_data = {
            "Input": received_text,
            "Output": translated_result
        }
        
        # Return JSON response
        return response_data

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")



##################################3 language detection #############################################################################3





@router.post("/detect")

async def detection_lang (input_data: TextInput): 

    try:
        received_text = input_data.text
        print (type(received_text))

            
       
        translated_result = predict_model(received_text)
        



  # Create a dictionary with the input and output texts
        response_data = {
            "Input": received_text,
            "Output": translated_result
        }
        
        # Return JSON response
        return response_data

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")




