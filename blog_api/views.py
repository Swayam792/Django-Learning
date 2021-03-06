from email import message
from rest_framework import generics,viewsets
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAdminUser,DjangoModelPermissions,BasePermission,SAFE_METHODS,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class PostUserwritePermission(BasePermission):
    message = 'Editing post is resticted to the author only'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user

class PostList(viewsets.ModelViewSet):
    permission_classes = [PostUserwritePermission]
    serializer_class = PostSerializer
    queryset = Post.postobject.all()

    def get_object(self,queryset=None,**kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post,title=item)

    def get_queryset(self):
        return Post.object.all()
        


           
# class PostList(viewsets.ViewSet):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     queryset = Post.postobject.all()

#     def list(self,request):
#         serializer_class = PostSerializer(self.queryset,many=True)
#         return Response(serializer_class.data)

#     def retrieve(self,request,pk=None):        
#         post = get_object_or_404(self.queryset, pk=pk)
#         serializer_class = PostSerializer(post)
#         return Response(serializer_class.data)



# class PostList(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     queryset = Post.postobject.all()
#     serializer_class = PostSerializer

# class PostDetail(generics.RetrieveUpdateDestroyAPIView,PostUserwritePermission):
#     permission_classes = [PostUserwritePermission]
#     queryset = Post.postobject.all()
#     serializer_class = PostSerializer
 