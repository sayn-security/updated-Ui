import java.awt.BorderLayout;
import java.awt.Container;
import java.awt.Dimension;
import java.awt.event.*;
import java.sql.Time;
import java.time.LocalTime;
import java.util.ArrayList;
import java.io.*;

import javax.swing.*;

public class KeyEventDemo extends JFrame implements KeyListener, ActionListener {
	/**
	 * 
	 */
	ArrayList<String> letters = new ArrayList<String>();
	ArrayList<LocalTime> timing = new ArrayList<LocalTime>();
	ArrayList<String> keysstring = new ArrayList<String>();
	static int global;
	private static final long serialVersionUID = -100468474145156277L;
	JTextArea displayArea;
	JTextField typingArea;
	static final String newline = System.getProperty("line.separator");

	public static void main(int k) throws IOException {
		
		/*String a = "blaaaaa: a :123412.1231231";
		int countcolon = 0;
		String number = null;
		for(int i = 0; i < a.length(); i++)
		{
			if(a.charAt(i) == ':')
				countcolon++;
			if(countcolon == 1)
			{
				number = a.substring(i+2);
			}
		}
		double num = Double.parseDouble(number);
		System.out.println(number + "\t" + num);
		*/
		global = k;
		/* Use an appropriate Look and Feel */
		try {
			// UIManager.setLookAndFeel("com.sun.java.swing.plaf.windows.WindowsLookAndFeel");
			// UIManager.setLookAndFeel("com.sun.java.swing.plaf.gtk.GTKLookAndFeel");
			UIManager.setLookAndFeel("javax.swing.plaf.metal.MetalLookAndFeel");
		} catch (UnsupportedLookAndFeelException ex) {
			ex.printStackTrace();
		} catch (IllegalAccessException ex) {
			ex.printStackTrace();
		} catch (InstantiationException ex) {
			ex.printStackTrace();
		} catch (ClassNotFoundException ex) {
			ex.printStackTrace();
		}
		/* Turn off metal's use of bold fonts */
		UIManager.put("swing.boldMetal", Boolean.FALSE);

		// Schedule a job for event dispatch thread:
		// creating and showing this application's GUI.
		javax.swing.SwingUtilities.invokeLater(new Runnable() {
			public void run() {
				createAndShowGUI();
			}
		});
		
		
	}

	/**
	 * Create the GUI and show it. For thread safety, this method should be
	 * invoked from the event-dispatching thread.
	 */
	private static void createAndShowGUI() {
		// Create and set up the window.
		KeyEventDemo frame = new KeyEventDemo("KeyEventDemo");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		// Set up the content pane.
		frame.addComponentsToPane();

		// Display the window.
		frame.pack();
		frame.setVisible(true);
	}

	private void addComponentsToPane() {

		JButton button = new JButton("Clear");
		button.addActionListener(this);

		typingArea = new JTextField(20);
		typingArea.addKeyListener(this);

		// Uncomment this if you wish to turn off focus
		// traversal. The focus subsystem consumes
		// focus traversal keys, such as Tab and Shift Tab.
		// If you uncomment the following line of code, this
		// disables focus traversal and the Tab events will
		// become available to the key event listener.
		// typingArea.setFocusTraversalKeysEnabled(false);

		displayArea = new JTextArea();
		displayArea.setEditable(false);
		JScrollPane scrollPane = new JScrollPane(displayArea);
		scrollPane.setPreferredSize(new Dimension(375, 125));

		getContentPane().add(typingArea, BorderLayout.PAGE_START);
		getContentPane().add(scrollPane, BorderLayout.CENTER);
		getContentPane().add(button, BorderLayout.PAGE_END);
	}

	public KeyEventDemo(String name) {
		super(name);
	}

	/** Handle the key typed event from the text field. */
	public void keyTyped(KeyEvent e) {
		try {
			displayInfo(e, "KEY TYPED: ");
		} catch (IOException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
	}

	/** Handle the key pressed event from the text field. */
	public void keyPressed(KeyEvent e) {
		try {
			displayInfo(e, "KEY PRESSED: ");
		} catch (IOException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
	}

	/** Handle the key released event from the text field. */
	public void keyReleased(KeyEvent e) {
		try {
			displayInfo(e, "KEY RELEASED: ");
		} catch (IOException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
	}

	/** Handle the button click. */
	public void actionPerformed(ActionEvent e) {
		// Clear the text components.
		displayArea.setText("");
		typingArea.setText("");

		// Return the focus to the typing area.
		typingArea.requestFocusInWindow();
	}
	
	int counterrrr = 0;
	/* THIS IS WHERE I SAVE THE KEYPRESS KEYRELEASE AND KEYTYPED INTO THE .TXT FILE 
	 * 
	 * 
	 */
	private void displayInfo(KeyEvent e, String keyStatus) throws IOException {

		// You should only rely on the key char if the event
		// is a key typed event.
		int id = e.getID();
		String keyString;
		if (id == KeyEvent.KEY_TYPED) {
			char c = e.getKeyChar();
			keyString = "key character = '" + c + "'";
		} else {
			int keyCode = e.getKeyCode();
			keyString = "key code = " + KeyEvent.getKeyText(keyCode);
		}

		letters.add(keyStatus);

		timing.add(java.time.LocalTime.now());
		
		keysstring.add(keyString);
		FileWriter fstream = new FileWriter("out"+global+".txt");
		BufferedWriter out = new BufferedWriter(fstream);
		for(int i = 0; i < letters.size(); i++)
		{
			out.write(letters.get(i) + "\t" + keysstring.get(i) + "\t" + timing.get(i) + "\n");
		}
		out.close();
		
	}
}