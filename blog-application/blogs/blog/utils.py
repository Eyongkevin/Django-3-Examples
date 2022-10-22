def search_filter(request, obj):
    q = request.GET.get("q")
    if q:
        return obj.filter(title__icontains=q)
    return obj
