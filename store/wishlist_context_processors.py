from .models import WishList

def wishlistcounter(request):
    wishlistcounter=0
    try:
        wishlist = WishList.objects.filter(user=request.user.id)
        
       
            
    except WishList.DoesNotExist:
        wishlistcounter = 0
    
    return dict(wishlistcounter=wishlistcounter)