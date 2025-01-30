from django.shortcuts import render
import yt_dlp

def youtube(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        format_id = request.POST.get('format_id')

        if not format_id:  
            # First submission: Get available formats
            formats = list_formats(link)
            return render(request, 'youtube.html', {'formats': formats, 'link': link})

        try:
            # Second submission: Download selected format
            ydl_opts = {
                'format': format_id,  # Download the chosen format
                'outtmpl': 'downloads/%(title)s.%(ext)s',
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
            
            return render(request, 'youtube.html', {'message': 'Video downloaded successfully!'})
        except yt_dlp.utils.DownloadError as e:
            return render(request, 'youtube.html', {'error': f'Error: {str(e)}'})

    return render(request, 'youtube.html')

def list_formats(video_url):
    ydl_opts = {}
    formats_list = []

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        formats = info_dict.get('formats', [])

        for f in formats:
            formats_list.append({
                'format_id': f['format_id'],
                'ext': f['ext'],
                'resolution': f.get('resolution', 'N/A'),
                'fps': f.get('fps', 'N/A'),
                'size': f.get('filesize', 'Unknown')
            })
    
    return formats_list
