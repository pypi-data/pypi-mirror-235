.. raw:: html

   <h1 align="center">

GetterSetter.

.. raw:: html

   </h1>

.. raw:: html

   <p align="center">

    Getter/Setter. Implements new syntax so you can implement getter and
    setter in one line.Originally its a part of volt but it can be used
    anywhere.

.. raw:: html

   </p>

From this:

.. code:: python

   class X:
     def set_text(self, text: str) -> None:
       """Set text."""
       self.o_text.setText(text)

     def get_text(self) -> str:
       """Get text."""
       return self.o_text.text

Later…:

.. code:: python

   text = X()

   text.set_text('x')

   print(text.get_text())

To this:

.. code:: python

   self.text = GetterSetter("default value", lambda new_text: self.o_text.setText(new_text))

Later…:

.. code:: python

   my_text = X()

   my_text.text[SET, 'my_text']

   print(my_text.text[GET])

Installation: `pip install getter_setter` **or** install
``getter_setter.py`` and move into your project directory.

.. raw:: html

   <hr>

.. raw:: html

   <p align="center">

    GetterSetter v1.0.

.. raw:: html

   </p>
