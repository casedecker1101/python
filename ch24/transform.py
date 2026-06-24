class transform:
    # return the top N records from the dataset
    def head(self, dataset, setp):
        if not dataset:
            raise Exception("Dataset cannot be empty.")
        if step < 1: 
            raise Exception("The step value must be positive.")
        return dataset[len(dataset) - step:len(dataset)]
    
    # return the last N records from the dataset
    def tail(self, dataset, step):
        if not dataset:
            raise Exception("Dataset cannot be empty.")
        if step < 1:
            raise Exception("The step value must be positive.")
        return dataset[len(dataset) - step:len(dataset)]
    
    # rename a column in the dataset
    def rename_attribute(self, dataset, attribute, new_attribute):
        if not dataset:
            raise Exception("Dataset cannot be empty.")
        if not attribute:
            raise Exception("The attribute key must be a valid key.")
        new_dataset = list()
        for row in dataset:
            if attribute in row.keys():
                val = row[attribute]
                new_row = row.copy()
                del new_row[attribute]
                new_row[new_attribute] = val
                new_dataset.append(new_row)
            else:
                raise Exception("Operation is not possible because the column " + str(column_name) + " does not exist in one of the rows in the dataset.")
        return dataset
    
    # remove a column from the dataset
    def remove_attribute(self, dataset, attribute):
        new_dataset = list()
        for row in dataset:
            new_row = row
            if attribute in new_row.keys():
                del new_row[attribute]
                new_dataset.append(new_row)
        return new_dataset
    
    def rename_attributes(self, dataset, attributes, new_attributes):
        if not attributes or not new_attributes:
            raise Exception("The attributes cannot be empty.")
        if len(attributes) != len(new_attributes):
            raise Exception("The number of new column names must match the number of existing column names.")
        new_dataset = list()
        for row in dataset:
            new_row = row
            for i in range(0, len(attributes)):
                attribute = attributes[i]
                new_attribute = new_attributes[i]
                if attribute in new_row.keys():
                    val = row[attribute]
                    del new_row[attribute]
                    new_row[new_attribute] = val
                else:
                    raise Exception("Operation is not possible because the key " + str(key) + " does not exist in one of the rows in the dataset.")
            new_dataset.append(new_row)
        return new_dataset
    
    # remove a column from the dataset
    def remove_attributes(self, dataset, attributes):
        if not dataset:
            raise Exception("Dataset cannot be empty")
        if not attributes:
            raise Exception("The list of attributes cannot be empty.")
        new_dataset = list()
        for row in dataset:
            new_row = row
            for attribute in attributes:
                if attribute in new_row.keys():
                    del new_row[attribute]
            new_dataset.append(new_row)
        return new_dataset
    
    def transform(self, dataset, attribute, new_attribute, transform_function, *args):
        if not dataset:
            raise Exception("Dataset cannot be empty.")
        if not attribute or not new_attribute:
            raise Exception("The transform_function cannot be None.")
        if not transform_function:
            raise Exception("The transform_function cannot be None.")
        new_dataset = list()
        for row in dataset: 
            t = transform_function(row[attribute], *args)
            z = row.copy()
            z.update({new_attribute:t}) # create new column in the data
            new_dataset.append(z)
        return new_dataset
    
    