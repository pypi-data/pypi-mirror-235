def set_LanguageModel_textsplitter(self, TheModel: str):
    """
    This function sets the language model to the choice of the user.
    However, it will first check whether the user asks for a valid model or not.
    As such, one should always use this setting-function instead of just
    blindly manipulating the class-parameter. In this case, the user
    can be sure that only a valid model is accepted.
    """
    
    # -----------------------------------------------------------------------
    
    # begin by setting the model to the default-value. It will stay this value
    # if the user ased for an invalid model:
    self.LanguageModel = "gpt-3.5-turbo"
    self.BackendChoice = "openai"
    
    # Next, define the array of allowed ChatCompletion models from OpenAI::
    ChatCompletion_Array = []
    ChatCompletion_Array.append("gpt-4")
    ChatCompletion_Array.append("gpt-4-0314")
    ChatCompletion_Array.append("gpt-4-32k")
    ChatCompletion_Array.append("gpt-4-32k-0314")
    ChatCompletion_Array.append("gpt-3.5-turbo")
    ChatCompletion_Array.append("gpt-3.5-turbo-0301")
    
    # Next, define the array of completion models from OpenAI:
    Completion_Array = []
    Completion_Array.append("text-davinci-003")
    Completion_Array.append("text-davinci-002")
    Completion_Array.append("text-curie-001")
    Completion_Array.append("text-babbage-001")
    Completion_Array.append("text-ada-001")

    # Next, define the array of models for huggingface:
    Huggingface_Array = []
    Huggingface_Array.append("TheBloke")
    
    # ATTENTION: We differentiate between the 2 openai-options by testing if the string contains "gpt" or not.
    # ATTENTION: tiktoken should also be able to support the model (not currently checked).
    
    # Next, test the arrays 1-by-1:
    if (TheModel in ChatCompletion_Array):
        self.LanguageModel = TheModel
        self.BackendChoice = "openai"
    elif (TheModel in Completion_Array):
        self.LanguageModel = TheModel
        self.BackendChoice = "openai"
    elif (TheModel in Huggingface_Array):
        self.LanguageModel = TheModel
        self.BackendChoice = "huggingface"
    else:
        
        # Then, we generate a message to state that an invalid model was used:
        print("\n\n ==> / ==> / ==> ERROR: Your model choice <" + str(TheModel) + "> is NOT a valid LLM!\n\n")
    
    # Done.
