import requests

cookies = {
    'XSRF-TOKEN': 'eyJpdiI6IjFHWlgvaHh1NVlFSldDa3plQzZ1UlE9PSIsInZhbHVlIjoiYVdVRVk2elcwZjYxL2xTanlMVnc3VUJDbjBIN24wTURSZFdNMFZjWnlkbmlqelczODAwdjdXblJ5a3lyWGlwM1ovaFFqbXhPdWYyKzR0SHgwcDZOTEh3c2FNU2kzY1ZCVTAyNUN1VnRLSE5mY3lDZDVOd0Zkb3JmeTFQa012UjIiLCJtYWMiOiJjMWE5N2ZmZGJlZjhhM2M2Y2U2YTRmYWYyMzBhMmRmODAyMmU0NzI4NzkyMGZkZDA4OTQ4NGMwYTE4OTVkMzYwIiwidGFnIjoiIn0%3D',
    'alta_ski_area_session': 'eyJpdiI6ImlIOVk4M3F1cmJ1QlRxUXM1MHlKaFE9PSIsInZhbHVlIjoiSVcvRVR1QnlMQ214b1krcUwxMDdoM2dPQkN6WHNlZDZHOFc5MHRCVEd3T0pwekhURHE5L2tvanhYc2V6SFJQWDZmTm5aMmZPbTQwNkVsc2ZDN1A4akFpL1ZmUVViL0ROU2xMOG10MFo0NFVGQ3N5MmViODhKQkZTSEttWkVIVGMiLCJtYWMiOiJmMDhiMzM4OTc5OTY3YjY1YTNjZGRkOGU2ZDlmMzFhM2I0NjIyY2Q4M2Q4OTc1NDc0OGJkMGQ5ZTQ0NjFkZGZiIiwidGFnIjoiIn0%3D',
    '_gcl_au': '1.1.712153471.1677600056',
    '_ga_BR1ET7XS8P': 'GS1.1.1677600056.1.0.1677600056.0.0.0',
    '_ga': 'GA1.2.1863688027.1677600056',
    '_gid': 'GA1.2.2084499848.1677600059',
    '_gat_UA-8608592-1': '1',
    '_fbp': 'fb.1.1677600062737.239123709',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    # 'Cookie': 'XSRF-TOKEN=eyJpdiI6IjFHWlgvaHh1NVlFSldDa3plQzZ1UlE9PSIsInZhbHVlIjoiYVdVRVk2elcwZjYxL2xTanlMVnc3VUJDbjBIN24wTURSZFdNMFZjWnlkbmlqelczODAwdjdXblJ5a3lyWGlwM1ovaFFqbXhPdWYyKzR0SHgwcDZOTEh3c2FNU2kzY1ZCVTAyNUN1VnRLSE5mY3lDZDVOd0Zkb3JmeTFQa012UjIiLCJtYWMiOiJjMWE5N2ZmZGJlZjhhM2M2Y2U2YTRmYWYyMzBhMmRmODAyMmU0NzI4NzkyMGZkZDA4OTQ4NGMwYTE4OTVkMzYwIiwidGFnIjoiIn0%3D; alta_ski_area_session=eyJpdiI6ImlIOVk4M3F1cmJ1QlRxUXM1MHlKaFE9PSIsInZhbHVlIjoiSVcvRVR1QnlMQ214b1krcUwxMDdoM2dPQkN6WHNlZDZHOFc5MHRCVEd3T0pwekhURHE5L2tvanhYc2V6SFJQWDZmTm5aMmZPbTQwNkVsc2ZDN1A4akFpL1ZmUVViL0ROU2xMOG10MFo0NFVGQ3N5MmViODhKQkZTSEttWkVIVGMiLCJtYWMiOiJmMDhiMzM4OTc5OTY3YjY1YTNjZGRkOGU2ZDlmMzFhM2I0NjIyY2Q4M2Q4OTc1NDc0OGJkMGQ5ZTQ0NjFkZGZiIiwidGFnIjoiIn0%3D; _gcl_au=1.1.712153471.1677600056; _ga_BR1ET7XS8P=GS1.1.1677600056.1.0.1677600056.0.0.0; _ga=GA1.2.1863688027.1677600056; _gid=GA1.2.2084499848.1677600059; _gat_UA-8608592-1=1; _fbp=fb.1.1677600062737.239123709',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

response = requests.get('https://www.alta.com/lift-terrain-status', cookies=cookies, headers=headers)

print(response.text)
