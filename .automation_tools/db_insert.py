import sqlite3

data = ['Eugene Adugbire Agomna', 'Mathew Akalagtota Anafo', 'Mercy Gbolowu', 'Millicent Owusu-Peprah', 'Fiifi Emmanuel Musah', 'Sandra Akwaa Cobbinah', 's Edem Cosmo Kemavor', 'Kwasi Elikplim Avor', 'Micheal Kwame Otoo', 'Mina Kromo Adu', 'Frederick Adu Poku', 'Judith Amudjie', 'Gifty Ahiatsi', 'Lydia Amissah', 'Makufi Abigail Hanyor', 'Samuel Appiah', 'Charity Konamah', 'Mercy Okyere', 'Sam Lawrencia Adwowa', 'Tonia Nurideen', 'Emmanuel Addo Osafo', 'Stephen Bandoma', 'Yaa Ndropengi', 'Vanessah Lanyoh', 'Florence Hope Mizero', 'Veronica Opoku', 'Williams Appiah', 'Worlanyo Kusi James', 'Angelique Ingabire', 'Michael Judith Lurit Lowrence', 'Kwabena Joseph Bebu',
        'Daniella Brobbey', 'Nsadha Elifazi', 'Philip Akwafo Tetteh', 'Alberta Baffour-Awuah', 'Kwetey Ezekiel Narh', 'Israel Safo', 'Joseph Kwame Nkrumah', 'Solomon Springs Mukundane', 'Otchere-Darko Ebenezer', 'Maina Kariuki Boniface', 'Kariuki Boniface Maina', 'Lydia Gyabaah', 'Dzagble Amekudzi Valeria', 'Seth Okyere', 'Edwin Amponsah', 'Okello Robert Ayella', 'Obeng Aniagyei Ransford', 'Ngongkum Injei Ida Kwam', 'Solomon Aboagye', 'Emmanuel Oduro', 'Alhassan Abubakari', 'Noye Joshua Agyemang', 'Kofi Israel Adokpoh', 'Maxwell Agyei Frimpong', 'Ngatir Anthony Mbugua', 'Juliet Kumi', 'Emily Otoo-Quayson', 'Bright Amanful', 'Clarisse Marie Mukanyandwi', 'Yussif Mahama', 'Alexander Abina', 'Amina Nakawooya', 'Emmanuel Wadekuu', 'Clifford Sheriff Ninson', 'N-Yong-Yiri Gaeten', 'Eunice Agyin', 'Atta Samuel Gyan', 'Kofi Williams Lasi', 'Mohammed Alhassan', 'Diane Iradukunda', 'Solomon Asare', 'Hero-Godsway K. Zilevu', 'Amina Nakawooya', 'Emmanuel Wadekuu', 'Agnes Dusi', 'Joel Ansah', 'Angelina Owusu', 'Boatemaa Francisca Ataa', 'Millicent Gurah', 'Theophilus Quaicoe', 'Harriet Afran', 'Mary Taylor', 'Hilda Bukari Kavala', 'Naziratu Seidu', 'Iddrisu Addul Hakeem', 'Issah Musah Aziba', 'Richmond Agyarkwa', 'Selina Asare', 'Gifty Apuri', 'Doris Nketia', 'Naa Balawuu Saeed Mariwa', 'Nancy Awinbisa Amiziah', 'Emelia Atabo', 'Saasi Arimiyaw', 'Aba Barnes Beatrice', 'Sandra Attitsogbui', 'Sandra Benedicta Adzato', 'Mawufemor Amuzu', 'Jallow Abdullah', 'Catherine Amandine Atasige', 'Bright Tetteh', 'Joana Aboagyewaa']

conn = sqlite3.connect('../db.sqlite3')

id = 47
batch = "2015/2016 Academic Year"

for _ in len(data):
    id+=1
    conn.execute(f"INSERT INTO app_cohortbatch (name, cohort_id) \
        VALUES ('{batch}', '{id}')")

