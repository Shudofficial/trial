import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.Timer;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class RacingGame extends JFrame {

    private final int WIDTH = 800;
    private final int HEIGHT = 600;
    private final int ROAD_WIDTH = 50;
    private final int CAR_WIDTH = 20;
    private final int CAR_HEIGHT = 40;
    private final int MAX_SPEED = 10;
    private int carX = (WIDTH - CAR_WIDTH) / 2;
    private int carY = HEIGHT - CAR_HEIGHT - 50;
    private int carSpeed = 0;
    private int roadLineOffset = 0;
    private Timer timer;
    private JPanel roadPanel;

    public RacingGame() {
        setTitle("Racing Game");
        setSize(WIDTH, HEIGHT);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setResizable(false);
        setVisible(true);

        roadPanel = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                g.setColor(Color.GRAY);
                g.fillRect(0, 0, WIDTH, HEIGHT);

                g.setColor(Color.WHITE);
                for (int y = roadLineOffset; y < HEIGHT; y += 50) {
                    g.fillRect((WIDTH - ROAD_WIDTH) / 2, y, ROAD_WIDTH, 30);
                }

                g.setColor(Color.RED);
                g.fillRect(carX, carY, CAR_WIDTH, CAR_HEIGHT);
            }
        };

        add(roadPanel);

        timer = new Timer(100, new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                carX += carSpeed;
                if (carX < (WIDTH - ROAD_WIDTH) / 2) {
                    carX = (WIDTH - ROAD_WIDTH) / 2;
                }
                if (carX > (WIDTH - ROAD_WIDTH) / 2 + ROAD_WIDTH - CAR_WIDTH) {
                    carX = (WIDTH - ROAD_WIDTH) / 2 + ROAD_WIDTH - CAR_WIDTH;
                }
                if (carSpeed > MAX_SPEED) {
                    carSpeed = MAX_SPEED;
                }
                if (carSpeed < -MAX_SPEED) {
                    carSpeed = -MAX_SPEED;
                }
                roadLineOffset += carSpeed;
                if (roadLineOffset >= 50) {
                    roadLineOffset -= 50;
                }
                if (roadLineOffset <= -50) {
                    roadLineOffset += 50;
                }
                roadPanel.repaint();
            }
        });
        timer.start();
    }

    public static void main(String[] args) {
        RacingGame game = new RacingGame();
    }
}
