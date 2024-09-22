# import docx
# import pandas as pd

# # i am not sure how you are getting your data, but you said it is a
# # pandas data frame
# df = pd.DataFrame({"qweq":[1,2,3,4,5,6],"12dsad":['12312axc','12312axc','12312axc','12312axc','12312axc','12312axc']})

# # open an existing document
# doc = docx.Document()

# # add a table to the end and create a reference variable
# # extra row is so we can add the header row
# t = doc.add_table(df.shape[0]+1, df.shape[1])
# t.style = 'LightShading-Accent1'
# # add the header rows.
# for j in range(df.shape[-1]):
#     t.cell(0,j).text = df.columns[j]

# # add the rest of the data frame
# for i in range(df.shape[0]):
#     for j in range(df.shape[-1]):
#         t.cell(i+1,j).text = str(df.values[i,j])

# # save the doc
# doc.save('test.docx')