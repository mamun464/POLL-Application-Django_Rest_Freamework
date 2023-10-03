from  django.http import JsonResponse
from .models import Author
from .models import Choice
from .serializer import AuthorSerializer,ChoiceSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# All qustion and author List
@api_view(['GET','POST'])
def question_list(request,format=None):
    if request.method == 'GET':
        question_data=Author.objects.all()
        voting_data=Choice.objects.all()
        
        question_data_serializer=AuthorSerializer(question_data,many=True)
        voting_data_serializer=ChoiceSerializer(voting_data,many=True)

        combined_Data=question_data_serializer.data+voting_data_serializer.data

        model_1=question_data_serializer.data
        model_2=voting_data_serializer.data

        combined_Data1=getCombined(model_1,model_2)
        
        return Response(combined_Data1)

  

# ID wise qustion and author List edit,deleted
@api_view(['GET','PUT', 'DELETE'])
def single_question(request,id,format=None):

    try:
        author=Author.objects.get(pk=id)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    try:
        
        vote=Choice.objects.get(pk=id)
    except Choice.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        author_data=AuthorSerializer(author)
        vote_data=ChoiceSerializer(vote)

        model_1=author_data.data
        model_2=vote_data.data


        combined_entry = {
                'id': model_1['id'],
                'author_name': model_1['author_name'],
                'author_question': model_1['author_question'],
                'Choice_Answer': model_2['Choice_Answer'],
                'vote': model_2['vote']
            }
            
        return Response(combined_entry)
    
    elif request.method == "PUT":
        author_serializer=AuthorSerializer(author,data=request.data)
        if author_serializer.is_valid():
                author_serializer.save()
                return Response(author_serializer.data)
        
        return Response(author_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    elif request.method == 'DELETE':
             author.delete()
             return Response(status=status.HTTP_204_NO_CONTENT)




def getCombined(model_1, model_2):
    combined_dict = {}

    # Create a dictionary for model_2 for faster lookup
    model_2_dict = {item['id']: item for item in model_2}

    for item_1 in model_1:
        id_1 = item_1['id']
        item_2 = model_2_dict.get(id_1)

        if item_2:
            combined_entry = {
                'id': id_1,
                'author_name': item_1['author_name'],
                'author_question': item_1['author_question'],
                'Choice_Answer': item_2['Choice_Answer'],
                'vote': item_2['vote']
            }
            combined_dict[id_1] = combined_entry

    return list(combined_dict.values())
