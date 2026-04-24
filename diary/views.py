from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Entry
from .forms import EntryForm


@login_required
def entry_list(request):
    entries = Entry.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'diary/entry_list.html', {'entries': entries})


@login_required
def search_entries(request):
    query = request.GET.get('q')
    if query:
        entries = Entry.objects.filter(
            author=request.user,
            title__icontains=query
        ) | Entry.objects.filter(
            author=request.user,
            content__icontains=query
        ).distinct()
    else:
        entries = Entry.objects.none()
    return render(request, 'diary/search_results.html', {
        'entries': entries,
        'query': query
    })


@login_required
def create_entry(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.author = request.user
            entry.save()
            messages.success(request, 'Entry created successfully!')
            return redirect('diary:view_entry', pk=entry.pk)
    else:
        form = EntryForm()
    return render(request, 'diary/create_entry.html', {'form': form})


@login_required
def view_entry(request, pk):
    entry = get_object_or_404(Entry, pk=pk, author=request.user)
    return render(request, 'diary/view_entry.html', {'entry': entry})


@login_required
def edit_entry(request, pk):
    entry = get_object_or_404(Entry, pk=pk, author=request.user)
    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, 'Entry updated successfully!')
            return redirect('diary:view_entry', pk=entry.pk)
    else:
        form = EntryForm(instance=entry)
    return render(request, 'diary/edit_entry.html', {'form': form, 'entry': entry})


@login_required
def delete_entry(request, pk):
    entry = get_object_or_404(Entry, pk=pk, author=request.user)
    if request.method == 'POST':
        entry.delete()
        messages.success(request, 'Entry deleted successfully!')
        return redirect('diary:entry_list')
    return render(request, 'diary/delete_entry.html', {'entry': entry})
