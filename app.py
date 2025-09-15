import streamlit as st

st.sidebar.image("logo.png")
st.sidebar.title('RpMusic')

generos = ['Trap', 'Rock', 'Rap', 'Hip-Hop',]

artistas = {
    "Rap": ["XXXtentacion", "Eminem", "Freddie Dredd"],
    "Trap": ["Travis Scott", "Teto", "Cochise"],
    "Rock": ["ACDC", "Guns and Roses", "Gorillaz"],
    "Hip-Hop": ["Tyler the Creator", "Tupac", "Jay z"]
}

genero_selecionado = st.sidebar.selectbox("Selecione o gênero:", generos)

if genero_selecionado:
    artistas = st.sidebar.selectbox(
        "Selecione o artista:", 
        artistas[genero_selecionado]
    )
    
if genero_selecionado and artistas:
    st.write(f"**Gênero:** {genero_selecionado}")
    st.write(f"**Artistas selecionado:** {artistas}")
    st.image(f'{artistas}.png', width=1000)
    st.markdown("---")
    
    if genero_selecionado == "Trap" and artistas == "Teto":
     st.video("https://www.youtube.com/watch?v=iDJM3HTdjck&list=RDiDJM3HTdjck&start_radio=1&pp=ygUSdGV0byBtdXN0YW5nIHByZXRvoAcB")
     st.link_button(url="https://open.spotify.com/playlist/37i9dQZF1DZ06evO3CL3a0",label="Spotify")
     
    elif genero_selecionado == "Trap" and artistas == "Travis Scott":
     st.video("https://youtu.be/ykMHDKB0-1o?list=RDykMHDKB0-1o")
     st.link_button(url="https://open.spotify.com/playlist/37i9dQZF1DZ06evO0vGf4I",label="Spotify")
     
    elif genero_selecionado == "Trap" and artistas == "Cochise":
     st.video("https://www.youtube.com/watch?v=MkzncIxhP9U&list=RDMkzncIxhP9U&start_radio=1&pp=ygUHY29jaGlzZaAHAdIHCQmyCQGHKiGM7w%3D%3D")
     st.link_button(url="https://open.spotify.com/playlist/37i9dQZF1E4qQJEaT0OWfk",label="Spotify")
     
    elif genero_selecionado == "Rap" and artistas == "XXXtentacion":
     st.video("https://youtu.be/GX8Hg6kWQYI?list=RDGX8Hg6kWQYI")
     st.link_button(url="https://open.spotify.com/playlist/37i9dQZF1DZ06evO0AnZXW",label="Spotify")
     
    elif genero_selecionado == "Rap" and artistas == "Eminem":
     st.video("https://youtu.be/lPlePBCS6Ic?list=RDlPlePBCS6Ic")
     st.link_button(url="https://open.spotify.com/playlist/37i9dQZF1DZ06evO4gTUOY",label="Spotify")
     
    elif genero_selecionado == "Rap" and artistas == "Freddie Dredd":
     st.video("https://youtu.be/8gkv8uYdMAA?list=RD8gkv8uYdMAA")
     st.link_button(url="https://open.spotify.com/playlist/37i9dQZF1E4q02Sea3ruPg",label="Spotify")
     
    elif genero_selecionado == "Rock" and artistas == "Gorillaz":
     st.video("https://youtu.be/04mfKJWDSzI?list=RD04mfKJWDSzI")
     st.link_button(url="https://open.spotify.com/playlist/37i9dQZF1DZ06evO25rXbO",label="Spotify")
     
    elif genero_selecionado == "Hip-Hop" and artistas == "Tyler the Creator":
     st.video("https://youtu.be/NmvVhovjJI0?list=RDNmvVhovjJI0")
     st.link_button(url="https://open.spotify.com/playlist/37i9dQZF1DZ06evO2T8209",label="Spotify")
     
    elif genero_selecionado == "Rock" and artistas == "ACDC":
     st.video("https://youtu.be/NhsK5WExrnE?list=RDNhsK5WExrnE")
     st.link_button(url="https://open.spotify.com/playlist/37i9dQZF1DZ06evO49hLQA",label="Spotify")
     
    elif genero_selecionado == "Rock" and artistas == "Guns and Roses":
     st.video("https://youtu.be/gXVGZv9Ya6w?list=RDgXVGZv9Ya6w")          
     st.link_button(url="https://open.spotify.com/playlist/37i9dQZF1DZ06evO1Ziym4",label="Spotify")
     
    elif genero_selecionado == "Hip-Hop" and artistas == "Tupac":
     st.video("https://youtu.be/fSq-4Dhwugg?list=RDfSq-4Dhwugg") 
     st.link_button(url="https://open.spotify.com/playlist/37i9dQZF1DZ06evO17QsVi",label="Spotify")
     
    elif genero_selecionado == "Hip-Hop" and artistas == "Jay z":
     st.video("https://youtu.be/odThhIA2gUM?list=RDodThhIA2gUM")
     st.link_button(url="https://open.spotify.com/playlist/37i9dQZF1E4Eo1x67VwxoH",label="Spotify")
     
     
   
      
    


    