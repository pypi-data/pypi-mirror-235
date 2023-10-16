.. _release_history:

Release and Version History
==============================================================================


x.y.z (Backlog)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


0.0.7 (2023-10-12)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Add a query parser to parse the handler input string into a structured query.

**Minor Improvements**

- The enter_handler, ctrl_a_handler, ctrl_w_handler, ctrl_p_handler will take an optional UI object as an argument.
- Bring ``T_ITEM`` and ``T_HANDLER`` type hint to the public API.


0.0.6 (2023-10-11)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Minor Improvements**

- Hit enter on error item can open the debug log automatically.

**Bugfixes**

- Fix another bug that the UI should not read the selected item when there's no item in the dropdown menu.


0.0.5 (2023-10-11)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Bugfixes**

- Fix a bug that the UI should not read the selected item when there's no item in the dropdown menu.


0.0.4 (2023-10-06)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Bugfixes**

- Fix the BACSPACE and CTRL + H key conflict issue on Windows.
- Fix the clear_items issue on Windows.


0.0.3 (2023-10-06)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Now the handler function take two arguments (it was one), the first argument is the query, the second argument is the UI, so developer could have more control to the underlying UI.
- Now the UI can automatically determine the max item to show and automatically truncate the title / subtitle based on terminal window size.
- Add support to capture and show error message in the UI.

**Miscellaneous**

- Now debugger can show what key is pressed.


0.0.2 (2023-10-05)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Rework the code base, add ``LineEdit`` and ``Dropdown`` module to manage the keyboard event handling logics.
- Now user can use keyboard to move cursor to left, right, up, down and be able to scroll the dropdown list.

**Miscellaneous**

- Add debugger.


0.0.1 (2023-10-04)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Implement the basic ``Render`` and ``UI`` module, it can simulate the Alfred Workflow UI in the Terminal.
