import sys, importlib
from enum import Enum


def edit(fields, tag='Edit'):
    yield '''export const UserEdit = () = > ('''
    yield f'<{tag} >< SimpleForm >'
    for name, field_info in model.model_fields.items():
        val = "validate={required()}" if field_info.required else ""
        if name == 'id':
            if tag == 'Edit':
                yield f'<TextInput  label="id" source="id" >/>'
        else:
            yield f'<TextInput  label="login" source="login" {val}>/>'
            if issubclass(field_info.annotation, Enum):
                choices = '[' + ','.join(f"{'id': '{f.name}', 'name': '{f.value}'}" for f in field_info.annotation) + ']'
                yield f'''<SelectInput source="role" {val} choices={{ {choices } }} />'''
    #         <ReferenceManyField label="Orders" reference="orders" target="user_real_id">
    #         <Datagrid>
    #         <ReferenceField source="service_id" reference="services" />
    #     <TextField source="link" />
    #     <TextField source="speed" />
    #     <TextField source="count" />
    #     <TextField source="cost" />
    #     <TextField source="progress" />
    #     <TextField source="status" />
    #     <EditButton />
    # </Datagrid>
    #
    # </ReferenceManyField>
    yield f'</SimpleForm></{tag}>'
    yield ');'

def listing(fields):
    yield 'export const ServiceList = () => ('
    yield 'const serviceFilters = ['
    yield '<SearchInput source="title" alwaysOn />,'
    yield '<ReferenceInput source="category_id" reference="categories" />,'
    yield '];'
    yield 'const ListToolbar = () => ('
    yield '<Stack direction="row" justifyContent="space-between">'
    yield '  <FilterLiveSearch source="q" label="Search" />'
    yield '  <FilterForm filters={serviceFilters} />'
    yield '  <div>'
    yield '      <FilterButton filters={serviceFilters} />'
    yield '      <CreateButton />'
    yield '  </div>'
    yield '</Stack>'
    yield ')'

    yield '<ListBase> <ListToolbar/> <List> <Datagrid>'
    for name, field_info in model.model_fields.items():
        yield f'<TextField  label="{field_info.title}" source="" />'
    yield '</Datagrid> </List> </ListBase>'
    yield ')'

def resource(name, model):
    yield '< Resource'
    yield f'name = "{name}'
    yield f'list = {{{model,__class__.__name__}List}}'
    yield f'edit = {{{model,__class__.__name__}Edit}}'
    yield f'create = {{{model,__class__.__name__}Create}}'
    yield '>'


if __name__ == '__name__':
    model = importlib.import_module(sys.argv[1])


    
