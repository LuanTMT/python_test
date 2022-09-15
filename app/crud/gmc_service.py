class GmcService:
    @classmethod
    def validate_page(cls,parameters:int= 1,page:bool= False) ->int:
        parameters=1 if parameters<1 else parameters
        if not page:
            parameters=100 if parameters>100 else parameters
        return parameters