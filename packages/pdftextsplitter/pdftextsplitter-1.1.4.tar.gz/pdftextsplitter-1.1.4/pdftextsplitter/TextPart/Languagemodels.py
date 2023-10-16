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
    
    # Next, define the array of allowed ChatCompletion models:
    ChatCompletion_Array = []
    ChatCompletion_Array.append("gpt-4")
    ChatCompletion_Array.append("gpt-4-0314")
    ChatCompletion_Array.append("gpt-4-32k")
    ChatCompletion_Array.append("gpt-4-32k-0314")
    ChatCompletion_Array.append("gpt-3.5-turbo")
    ChatCompletion_Array.append("gpt-3.5-turbo-0301")
    
    # Next, define the array of completion models:
    Completion_Array = []
    Completion_Array.append("text-davinci-003")
    Completion_Array.append("text-davinci-002")
    Completion_Array.append("text-curie-001")
    Completion_Array.append("text-babbage-001")
    Completion_Array.append("text-ada-001")
    
    # ATTENTION: We differentiate between the options by testing if the string contains "gpt" or not.
    # ATTENTION: tiktoken should also be able to support the model (not currently checked).
    
    # Next, test the arrays 1-by-1:
    if (TheModel in ChatCompletion_Array): self.LanguageModel = TheModel
    elif (TheModel in Completion_Array): self.LanguageModel = TheModel
    else:
        
        # Then, we generate a message to state that an invalid model was used:
        print("\n\n ==> / ==> / ==> ERROR: Your model choice <" + str(TheModel) + "> is NOT a valid OpenAI-model!\n\n")
    
    # Done.
